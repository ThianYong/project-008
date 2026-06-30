import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Project 008",
    page_icon="👋",
    layout="wide",
)

st.title("Hello world!")
st.write("This is Project 008 running on Streamlit.")
st.caption("Test app created from ChatGPT via GitHub connector.")

st.divider()

st.subheader("Hover icon test")
st.write(
    "Below is a Streamlit-friendly hover icon demo inspired by Its Hover. "
    "The original library is React + Motion based, so this page uses inline SVG and CSS animations instead."
)

components.html(
    """
    <style>
      :root {
        color-scheme: light;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      .hover-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(130px, 1fr));
        gap: 16px;
        padding: 8px 4px 18px;
      }
      .icon-card {
        border: 1px solid rgba(15, 23, 42, 0.12);
        border-radius: 18px;
        padding: 20px 16px;
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
        text-align: center;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
        cursor: default;
      }
      .icon-card:hover {
        transform: translateY(-5px);
        border-color: rgba(37, 99, 235, 0.35);
        box-shadow: 0 18px 42px rgba(15, 23, 42, 0.12);
      }
      .icon-card svg {
        width: 58px;
        height: 58px;
        stroke: #0f172a;
        stroke-width: 1.9;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
        transition: transform 220ms ease, stroke 220ms ease;
      }
      .icon-card:hover svg {
        transform: scale(1.08) rotate(-3deg);
        stroke: #2563eb;
      }
      .icon-card:hover .pulse {
        animation: pulse 900ms ease-in-out infinite alternate;
      }
      .icon-card:hover .slide {
        animation: slide 700ms ease-in-out infinite alternate;
      }
      .icon-card:hover .spin {
        transform-origin: 50% 50%;
        animation: spin 1200ms linear infinite;
      }
      .icon-title {
        margin-top: 12px;
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
      }
      .icon-note {
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
      }
      @keyframes pulse {
        from { opacity: 0.45; transform: scale(0.96); }
        to { opacity: 1; transform: scale(1.06); }
      }
      @keyframes slide {
        from { transform: translateX(-3px); }
        to { transform: translateX(4px); }
      }
      @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
      @media (max-width: 700px) {
        .hover-grid { grid-template-columns: repeat(2, minmax(120px, 1fr)); }
      }
    </style>

    <div class="hover-grid">
      <div class="icon-card" aria-label="Plug connected icon">
        <svg viewBox="0 0 64 64" role="img">
          <path d="M22 10v12" />
          <path d="M42 10v12" />
          <path d="M18 22h28v11a14 14 0 0 1-28 0z" />
          <path class="slide" d="M32 47v7" />
          <path class="pulse" d="M25 54h14" />
        </svg>
        <div class="icon-title">Plug</div>
        <div class="icon-note">connection hover</div>
      </div>

      <div class="icon-card" aria-label="AI spark icon">
        <svg viewBox="0 0 64 64" role="img">
          <path class="pulse" d="M32 8l4.5 15.5L52 28l-15.5 4.5L32 48l-4.5-15.5L12 28l15.5-4.5z" />
          <path d="M50 45l1.8 6.2L58 53l-6.2 1.8L50 61l-1.8-6.2L42 53l6.2-1.8z" />
        </svg>
        <div class="icon-title">AI</div>
        <div class="icon-note">spark animation</div>
      </div>

      <div class="icon-card" aria-label="Cloud deploy icon">
        <svg viewBox="0 0 64 64" role="img">
          <path d="M22 46h27a9 9 0 0 0 1.2-17.9A15 15 0 0 0 21.4 23 11.5 11.5 0 0 0 22 46z" />
          <path class="slide" d="M32 42V27" />
          <path class="slide" d="M25 34l7-7 7 7" />
        </svg>
        <div class="icon-title">Deploy</div>
        <div class="icon-note">GitHub to Streamlit</div>
      </div>

      <div class="icon-card" aria-label="Settings gear icon">
        <svg viewBox="0 0 64 64" role="img">
          <circle cx="32" cy="32" r="7" />
          <path class="spin" d="M32 10v7M32 47v7M10 32h7M47 32h7M16.4 16.4l5 5M42.6 42.6l5 5M47.6 16.4l-5 5M21.4 42.6l-5 5" />
        </svg>
        <div class="icon-title">Settings</div>
        <div class="icon-note">spin on hover</div>
      </div>
    </div>
    """,
    height=260,
)

st.info(
    "Source reference: Its Hover is an animated icon library built with React and Motion. "
    "This Streamlit test uses a lightweight inline-SVG adaptation for Python deployment."
)
