import streamlit as st
from pattern_generator import ComplexPatternGenerator
from script import example_patterns

st.set_page_config(page_title="Pattern Generator", layout="centered")

st.title("🎨 Live Pattern Generator")
st.markdown("Easily generate complex patterns using a structured definition.")

with st.expander("ℹ️ How to Use", expanded=False):
    st.write("Enter a pattern definition in the text area and optionally provide a name. Click **Generate Pattern** to see the result.")

pattern_input = st.text_area("📝 Enter Pattern Definition:", height=200, placeholder="[* ,5],3")
pattern_name_input = st.text_input("🏷️ Pattern Name (optional):", value="")

st.markdown("<style>div.stButton > button { width: 100%; }</style>", unsafe_allow_html=True)

if st.button("🚀 Generate Pattern"):
    if not pattern_input:
        st.error("⚠️ Please enter a pattern definition.")
    else:
        try:
            generator = ComplexPatternGenerator(justify_size=True, auto_index=False)
            pattern_name = pattern_name_input if pattern_name_input else "Custom Pattern"
            generated_pattern = generator.generate(pattern_input, pattern_name=pattern_name)

            st.success("✅ Pattern successfully generated!")
            st.subheader(f"📌 Generated Pattern: {pattern_name}")
            st.code(generated_pattern, language="plaintext")

        except Exception as e:
            st.error(f"❌ Error generating pattern: {e}")
            st.error("Please check your pattern definition syntax.")

st.markdown("---")
with st.expander("📂 Example Patterns (Click to Expand)"):
    for name, code in example_patterns.items():
        st.write(f"**{name}**:")
        st.code(code, language="plaintext")
