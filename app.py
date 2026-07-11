"""
Carnatic Ragam AI Chatbot
Expert AI assistant for Carnatic classical music — ragam identification and details.
Built with Groq (LLaMA-3.3-70B) + Gradio | Deploy-ready for Render
"""

import os
import re
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

from ragam_data import (
    RAGAM_DATABASE,
    SONG_TO_RAGAM,
    get_ragam_info,
    detect_ragam_from_song,
    get_all_ragam_names,
    format_ragam_for_prompt,
    build_full_knowledge_context,
)

# ── Environment ───────────────────────────────────────────────────────────────
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Add it to your .env file locally or to Render environment variables."
    )

client = Groq(api_key=GROQ_API_KEY)
MODEL = "llama-3.3-70b-versatile"

# ── System Prompt ─────────────────────────────────────────────────────────────
RAGAM_SUMMARY = build_full_knowledge_context()
ALL_RAGAM_NAMES = ", ".join(get_all_ragam_names())

SYSTEM_PROMPT = f"""You are **Ragam Guru**, an expert AI assistant specializing in Carnatic classical music, with deep knowledge of:
- All 72 Melakartha ragas and hundreds of Janya ragas
- Arohana (ascending scale) and Avarohana (descending scale) of every raga
- Vadi (primary note), Samvadi (secondary note), and characteristic phrases (prayogas)
- Gamaka (ornamentations) and their role in each raga
- Time of day, season, mood, and rasa (emotional essence) of ragas
- Famous compositions (krithis) by Tyagaraja, Muthuswami Dikshitar, Shyama Shastri, and other composers
- Song-to-raga mappings for thousands of classical and film songs
- Melakartha system, the 72 parent scales, and their janya derivatives
- Carnatic music concepts: tala, shruti, gamaka, sangati, alapana, neraval, swaraprastara

## YOUR KNOWLEDGE BASE
You have access to detailed data for these ragams in your internal database:
{RAGAM_SUMMARY}

## RAGAMS IN DATABASE
{ALL_RAGAM_NAMES}

## HOW TO RESPOND

### When asked about a specific RAGAM:
Provide a comprehensive response covering:
1. 🎵 **Full Name & Number** (Melakartha number if applicable)
2. 📈 **Arohana** (ascending scale with swara names)
3. 📉 **Avarohana** (descending scale)
4. 🎯 **Vadi & Samvadi** (jeeva swaras)
5. ⏰ **Time & Season** (when to sing/play)
6. 💫 **Mood & Rasa** (emotional character)
7. 🎼 **Famous Compositions** (by the Trinity and others)
8. 🎬 **Famous Film Songs** (if any)
9. 📝 **Description** (what makes this raga unique)

### When asked to IDENTIFY a raga from a song name:
1. Identify the raga from your knowledge
2. Explain why the song belongs to that raga
3. Give 2-3 other songs in the same raga as examples
4. Provide key details about the raga

### When asked CONCEPTUAL questions (melakartha, gamaka, etc.):
Give a clear, scholarly yet accessible explanation with examples.

### When comparing ragas:
Highlight the key differences in arohana/avarohana, mood, and characteristic phrases.

## TONE & STYLE
- Be friendly, scholarly, and enthusiastic about Carnatic music
- Use proper Carnatic terminology (arohana, avarohana, swara, gamaka, etc.)
- When using swara notation, use: S R1/R2/R3 G1/G2/G3 M1/M2 P D1/D2/D3 N1/N2/N3
- Use emoji sparingly to make responses visually appealing
- If you don't know a specific song's raga, say so honestly but try to help with related information
- Always encourage the user to explore more about Carnatic music

## SWARA NOTATION KEY
Sa(S), Ri(R1=Shuddha, R2=Chatushruti, R3=Shatshruti), 
Ga(G1=Shuddha, G2=Sadharana, G3=Antara), 
Ma(M1=Shuddha, M2=Prathi/Tivra), Pa(P), 
Dha(D1=Shuddha, D2=Chatushruti, D3=Shatshruti), 
Ni(N1=Shuddha, N2=Kaisika, N3=Kakali)
"""

# ── Ragam Detection Logic ─────────────────────────────────────────────────────

def extract_context_from_message(message: str) -> str:
    """
    Check if the user is asking about a known song or ragam.
    If found, inject detailed ragam context into the conversation.
    """
    msg_lower = message.lower()

    # Check for song-based raga detection
    detected = detect_ragam_from_song(message)
    if detected:
        return (
            f"\n\n[INTERNAL CONTEXT — Use this in your response]\n"
            f"The song mentioned matches this ragam in the database:\n"
            f"{format_ragam_for_prompt(detected)}\n"
        )

    # Check for direct ragam name mention
    for key, ragam in RAGAM_DATABASE.items():
        ragam_name = ragam["name"].lower()
        if ragam_name in msg_lower:
            return (
                f"\n\n[INTERNAL CONTEXT — Use this in your response]\n"
                f"The user is asking about this ragam from the database:\n"
                f"{format_ragam_for_prompt(ragam)}\n"
            )
        # Check aliases
        for alias in ragam.get("aliases", []):
            if alias.lower() in msg_lower:
                return (
                    f"\n\n[INTERNAL CONTEXT — Use this in your response]\n"
                    f"The user mentioned '{alias}' which matches ragam '{ragam['name']}':\n"
                    f"{format_ragam_for_prompt(ragam)}\n"
                )

    return ""


# ── Chat Function ─────────────────────────────────────────────────────────────

def chat(message: str, history: list[dict]) -> str:
    """
    Main chat function. Accepts a user message and conversation history,
    returns the assistant's response string.
    """
    if not message.strip():
        return "Please ask me something about Carnatic music! 🎵"

    # Build message list for the API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Add conversation history
    for turn in history:
        messages.append({"role": turn["role"], "content": turn["content"]})

    # Enrich the user message with ragam context if applicable
    context = extract_context_from_message(message)
    enriched_message = message + context

    messages.append({"role": "user", "content": enriched_message})

    # Call Groq API with streaming
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
        stream=True,
    )

    # Stream response
    response = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        response += delta
        yield response


# ── Gradio UI ─────────────────────────────────────────────────────────────────

TITLE = "🎵 Ragam Guru — Carnatic Music AI"
DESCRIPTION = """
<div style="text-align: center; padding: 10px 0;">
  <h2 style="color: #FF6B35; margin-bottom: 8px;">🎵 Ragam Guru</h2>
  <p style="font-size: 1.05em; color: #666; max-width: 700px; margin: 0 auto;">
    Your expert AI companion for <strong>Carnatic classical music</strong>.<br>
    Ask about any <em>ragam</em>, identify the raga of a song, or learn Carnatic music concepts.
  </p>
</div>
"""

EXAMPLES = [
    ["What ragam is Entharo Mahanubhavulu?"],
    ["Tell me everything about Kalyani ragam"],
    ["What is the difference between Bhairavi and Sindhu Bhairavi?"],
    ["Which ragas are suitable for early morning?"],
    ["Explain the Melakartha system in Carnatic music"],
    ["What is the mood of Hindolam raga?"],
    ["List some ragas that evoke sadness"],
    ["What ragam is Vatapi Ganapatim?"],
    ["Tell me about Hamsadhwani"],
    ["How does gamaka work in Carnatic music?"],
    ["What is the difference between Mohanam and Hamsadhwani?"],
    ["Which raga is used for lullabies?"],
]

THEME = gr.themes.Soft(
    primary_hue="orange",
    secondary_hue="amber",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "sans-serif"],
)

with gr.Blocks(
    theme=THEME,
    title="Ragam Guru — Carnatic Music AI",
    css="""
    /* ── Global ── */
    body { background: #0f0f0f; }

    /* ── Header ── */
    .ragam-header {
        background: linear-gradient(135deg, #1a0a00 0%, #2d1200 50%, #1a0a00 100%);
        border: 1px solid #FF6B35;
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 20px;
        box-shadow: 0 0 40px rgba(255, 107, 53, 0.15);
    }
    .ragam-header h1 {
        color: #FF6B35;
        font-size: 2.2em;
        font-weight: 800;
        margin: 0 0 8px 0;
        letter-spacing: -0.5px;
    }
    .ragam-header p {
        color: #c9a882;
        font-size: 1.05em;
        margin: 0;
        line-height: 1.6;
    }
    .ragam-header .tagline {
        color: #FFD700;
        font-weight: 600;
        font-size: 0.95em;
        margin-top: 10px;
    }

    /* ── Chat messages ── */
    .message.bot {
        background: linear-gradient(135deg, #1e1208, #2a1a0a) !important;
        border-left: 3px solid #FF6B35 !important;
        border-radius: 12px !important;
    }
    .message.user {
        background: linear-gradient(135deg, #0a1a2e, #0d2440) !important;
        border-left: 3px solid #4A9EFF !important;
        border-radius: 12px !important;
    }

    /* ── Chatbot container ── */
    #chatbot {
        background: #0d0d0d !important;
        border: 1px solid #2a1a0a !important;
        border-radius: 16px !important;
    }

    /* ── Input row ── */
    #msg-input textarea {
        background: #1a1a1a !important;
        color: #e8d5c4 !important;
        border: 1px solid #3a2510 !important;
        border-radius: 12px !important;
        font-size: 1em !important;
    }
    #msg-input textarea:focus {
        border-color: #FF6B35 !important;
        box-shadow: 0 0 0 2px rgba(255, 107, 53, 0.2) !important;
    }

    /* ── Submit button ── */
    #submit-btn {
        background: linear-gradient(135deg, #FF6B35, #FF8C5A) !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1em !important;
        color: white !important;
        transition: all 0.2s ease !important;
    }
    #submit-btn:hover {
        background: linear-gradient(135deg, #e55a22, #FF6B35) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4) !important;
    }

    /* ── Clear button ── */
    #clear-btn {
        background: #1a1a1a !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
        color: #888 !important;
    }
    #clear-btn:hover {
        border-color: #FF6B35 !important;
        color: #FF6B35 !important;
    }

    /* ── Examples section ── */
    .examples-header {
        color: #FF6B35;
        font-weight: 700;
        font-size: 0.95em;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 16px 0 8px 0;
    }
    .gr-sample-textbox {
        background: #1a1200 !important;
        border: 1px solid #3a2510 !important;
        border-radius: 8px !important;
        color: #e8d5c4 !important;
        font-size: 0.9em !important;
        transition: all 0.2s ease !important;
    }
    .gr-sample-textbox:hover {
        border-color: #FF6B35 !important;
        background: #2a1a08 !important;
        transform: translateY(-1px) !important;
    }

    /* ── Stats bar ── */
    .stats-bar {
        background: #111;
        border: 1px solid #222;
        border-radius: 10px;
        padding: 10px 16px;
        display: flex;
        gap: 20px;
        font-size: 0.85em;
        color: #888;
        margin-top: 12px;
    }
    .stats-bar span { color: #FF6B35; font-weight: 700; }

    /* ── Accordion ── */
    .gr-accordion {
        background: #111 !important;
        border: 1px solid #222 !important;
        border-radius: 12px !important;
    }
    """,
) as demo:

    # ── Header ──────────────────────────────────────────────────────────────
    gr.HTML(f"""
    <div class="ragam-header">
        <h1>🎵 Ragam Guru</h1>
        <p>
            Your expert AI companion for <strong>Carnatic classical music</strong>.
            Powered by <strong>Groq · LLaMA 3.3 70B</strong>.
        </p>
        <p class="tagline">
            🎼 Identify ragas from song names &nbsp;|&nbsp;
            📚 Explore raga details &nbsp;|&nbsp;
            🕉️ Learn Carnatic concepts
        </p>
        <div class="stats-bar">
            <div>Ragas in database: <span>{len(RAGAM_DATABASE)}</span></div>
            <div>Songs mapped: <span>{len(SONG_TO_RAGAM)}</span></div>
            <div>Powered by: <span>LLaMA 3.3 70B · Groq</span></div>
        </div>
    </div>
    """)

    # ── Chat Interface ───────────────────────────────────────────────────────
    chatbot = gr.Chatbot(
        elem_id="chatbot",
        label="Ragam Guru",
        height=520,
        type="messages",
        show_copy_button=True,
        avatar_images=(
            None,  # user avatar
            "https://api.dicebear.com/7.x/bottts/svg?seed=ragam&backgroundColor=FF6B35",  # bot
        ),
        placeholder=(
            "<div style='text-align:center; padding: 60px 20px; color: #555;'>"
            "<div style='font-size: 3em; margin-bottom: 16px;'>🎵</div>"
            "<div style='font-size: 1.2em; color: #777;'>Ask Ragam Guru anything about Carnatic music</div>"
            "<div style='font-size: 0.9em; color: #444; margin-top: 8px;'>"
            "Try: \"What ragam is Vatapi Ganapatim?\" or \"Tell me about Kalyani\"</div>"
            "</div>"
        ),
    )

    with gr.Row():
        msg_input = gr.Textbox(
            elem_id="msg-input",
            placeholder="Ask about any ragam, song, or Carnatic music concept...",
            show_label=False,
            scale=9,
            lines=1,
            max_lines=4,
        )
        submit_btn = gr.Button("Ask 🎵", elem_id="submit-btn", scale=1, variant="primary")

    with gr.Row():
        clear_btn = gr.Button("🗑️ Clear Chat", elem_id="clear-btn", size="sm")

    # ── Examples ─────────────────────────────────────────────────────────────
    gr.HTML('<div class="examples-header">💡 Try these questions</div>')
    gr.Examples(
        examples=EXAMPLES,
        inputs=msg_input,
        label="",
    )

    # ── Info Accordion ────────────────────────────────────────────────────────
    with gr.Accordion("ℹ️ About Ragam Guru", open=False):
        gr.Markdown(f"""
        ### What can Ragam Guru do?

        | Capability | Example |
        |---|---|
        | Identify raga from song | *"What ragam is Entharo Mahanubhavulu?"* |
        | Full raga details | *"Tell me about Kalyani"* |
        | Compare ragas | *"Difference between Bhairavi and Sindhu Bhairavi?"* |
        | Time/mood-based | *"Which ragas evoke sadness?"* |
        | Carnatic concepts | *"What is the Melakartha system?"* |
        | Gamaka & ornaments | *"How does gamaka work in Carnatic music?"* |

        ### Ragas in Database
        {', '.join(get_all_ragam_names())}

        ### Technology
        - **AI Model**: LLaMA 3.3 70B via Groq API (streaming)
        - **Frontend**: Gradio
        - **Knowledge Base**: Custom curated Carnatic ragam database
        """)

    # ── Event Handlers ────────────────────────────────────────────────────────
    def user_message(message, history):
        """Add user message to history."""
        history = history or []
        history.append({"role": "user", "content": message})
        return "", history

    def bot_response(history):
        """Generate and stream bot response."""
        if not history:
            return history
        last_user_msg = history[-1]["content"]
        history.append({"role": "assistant", "content": ""})
        for partial_response in chat(last_user_msg, history[:-1]):
            history[-1]["content"] = partial_response
            yield history

    # Submit via button
    submit_event = (
        msg_input.submit(user_message, [msg_input, chatbot], [msg_input, chatbot], queue=False)
        .then(bot_response, chatbot, chatbot)
    )
    submit_btn.click(user_message, [msg_input, chatbot], [msg_input, chatbot], queue=False).then(
        bot_response, chatbot, chatbot
    )

    # Clear chat
    clear_btn.click(lambda: [], None, chatbot)


# ── Launch ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.queue()
    demo.launch(
        server_name="0.0.0.0",   # Required for Render deployment
        server_port=port,
        show_error=True,
    )
