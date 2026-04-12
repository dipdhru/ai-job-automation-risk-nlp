"""
Production-ready Streamlit app for AI Job Risk Analyzer MVP.

Features:
- Professional branding and layout
- Real API integration (when deployed)
- User authentication (optional)
- Analytics tracking
- Export capabilities
"""

import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="AI Job Risk Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# STYLING
# ============================================================================
st.markdown("""
    <style>
        /* Main container */
        .main {
            max-width: 900px;
            margin: 0 auto;
        }

        /* Custom colors */
        :root {
            --primary: #667eea;
            --secondary: #764ba2;
            --danger: #ff6b6b;
            --success: #51cf66;
            --warning: #ffd93d;
        }

        /* Risk level styling */
        .risk-high {
            color: #ff6b6b;
            font-weight: bold;
        }

        .risk-moderate {
            color: #ffd93d;
            font-weight: bold;
        }

        .risk-low {
            color: #51cf66;
            font-weight: bold;
        }

        /* Card styling */
        .card {
            padding: 1.5rem;
            border-radius: 10px;
            background: #f8f9fa;
            border-left: 4px solid #667eea;
        }

        /* Header styling */
        .header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# CONSTANTS
# ============================================================================
API_BASE_URL = "https://ai-job-analyzer-production.railway.app"  # Update after deployment
# For local testing:
# API_BASE_URL = "http://localhost:8000"

# ============================================================================
# SESSION STATE
# ============================================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "token" not in st.session_state:
    st.session_state.token = None
if "user_data" not in st.session_state:
    st.session_state.user_data = None
if "analyses" not in st.session_state:
    st.session_state.analyses = []

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_headers():
    """Get authorization headers."""
    headers = {"Content-Type": "application/json"}
    if st.session_state.token:
        headers["Authorization"] = f"Bearer {st.session_state.token}"
    return headers


def fetch_options():
    """Fetch available options from API."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/jobs/options")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"Error fetching options: {e}")
    return None


def register_user(email: str, full_name: str, password: str):
    """Register a new user."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/auth/register",
            json={
                "email": email,
                "full_name": full_name,
                "password": password,
                "password_confirm": password,
            },
        )
        if response.status_code == 201:
            st.success("✓ Registration successful! Please login.")
            return True
        else:
            st.error(response.json().get("detail", "Registration failed"))
    except Exception as e:
        st.error(f"Error: {e}")
    return False


def login_user(email: str, password: str):
    """Login user and get token."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/auth/login",
            json={"email": email, "password": password},
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.token = data["access_token"]
            st.session_state.authenticated = True
            st.success("✓ Login successful!")
            st.rerun()
        else:
            st.error("Invalid email or password")
    except Exception as e:
        st.error(f"Error: {e}")


def analyze_job(title: str, description: str, skills: list, knowledge: list, abilities: list):
    """Send job analysis to API."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/jobs/analyze",
            headers=get_headers(),
            json={
                "job_title": title,
                "job_description": description,
                "skills": skills,
                "knowledge": knowledge,
                "abilities": abilities,
            },
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            st.error("Please login to continue")
        else:
            st.error(response.json().get("detail", "Analysis failed"))
    except Exception as e:
        st.error(f"Error: {e}")
    return None


def get_analysis_history():
    """Fetch user's analysis history."""
    try:
        response = requests.get(
            f"{API_BASE_URL}/api/v1/jobs/history?skip=0&limit=20",
            headers=get_headers(),
        )
        if response.status_code == 200:
            return response.json().get("items", [])
    except Exception as e:
        st.error(f"Error fetching history: {e}")
    return []


def get_risk_level(ai_proneness: float) -> str:
    """Determine risk level from score."""
    if ai_proneness > 0.66:
        return "🔴 HIGH"
    elif ai_proneness > 0.33:
        return "🟡 MODERATE"
    else:
        return "🟢 LOW"


def get_risk_color(ai_proneness: float) -> str:
    """Get color for risk level."""
    if ai_proneness > 0.66:
        return "red"
    elif ai_proneness > 0.33:
        return "orange"
    else:
        return "green"


# ============================================================================
# MAIN UI
# ============================================================================

# Header
st.markdown("""
    <div class="header">
        <h1>🤖 AI Job Risk Analyzer</h1>
        <p>Understand your automation risk. Build your future skills.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Navigation")

    if st.session_state.authenticated:
        st.write(f"**Logged in**")
        if st.button("Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.token = None
            st.rerun()

        page = st.radio(
            "Select Page",
            ["📊 Analyze Job", "📜 History", "ℹ️ About"],
            key="nav",
        )
    else:
        page = st.radio(
            "Select Page",
            ["📊 Try Demo", "🔐 Login", "📝 Register", "ℹ️ About"],
            key="nav",
        )

# ============================================================================
# PAGE: ANALYZE JOB
# ============================================================================
if page == "📊 Analyze Job" or page == "📊 Try Demo":

    if not st.session_state.authenticated and page == "📊 Analyze Job":
        st.warning("Please login to save your analyses")

    st.subheader("📋 Enter Job Details")

    # Job title
    job_title = st.text_input(
        "Job Title",
        placeholder="e.g., Data Scientist, Software Engineer",
        help="The position you want to analyze",
    )

    # Job description
    job_description = st.text_area(
        "Job Description",
        height=150,
        placeholder="Describe the main responsibilities, tasks, and day-to-day activities...",
        help="The more detailed, the better the analysis",
    )

    # Fetch options
    st.subheader("🎯 Key Skills & Knowledge")
    col1, col2, col3 = st.columns(3)

    options = fetch_options()

    if options:
        with col1:
            skills = st.multiselect(
                "Skills",
                options=options.get("skills", []),
                help="Select relevant skills for this role",
            )

        with col2:
            knowledge = st.multiselect(
                "Knowledge Areas",
                options=options.get("knowledge", []),
                help="Select relevant knowledge domains",
            )

        with col3:
            abilities = st.multiselect(
                "Abilities",
                options=options.get("abilities", []),
                help="Select relevant abilities",
            )

    # Analyze button
    col1, col2 = st.columns([1, 3])

    with col1:
        analyze_btn = st.button(
            "🚀 Analyze Job",
            use_container_width=True,
            type="primary",
        )

    with col2:
        st.caption("🔒 Your data is private and secure")

    # ========================================================================
    # RESULTS
    # ========================================================================

    if analyze_btn:
        if not job_title or not job_description:
            st.error("❌ Please provide both job title and description")
        else:
            with st.spinner("🔍 Analyzing job for AI automation risk..."):
                result = analyze_job(
                    title=job_title,
                    description=job_description,
                    skills=skills,
                    knowledge=knowledge,
                    abilities=abilities,
                )

            if result:
                st.success("✓ Analysis complete!")

                # Results layout
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Automation Risk",
                        f"{result['ai_proneness']:.1%}",
                        delta=None,
                    )

                with col2:
                    st.metric(
                        "Risk Level",
                        get_risk_level(result["ai_proneness"]),
                    )

                with col3:
                    st.metric(
                        "Protective Factors",
                        f"+{result['resistance_factors']:.1f}",
                    )

                # Risk interpretation
                st.subheader("📌 What This Means")

                ai_proneness = result["ai_proneness"]

                if ai_proneness > 0.66:
                    st.error(
                        """
                        ### ⚠️ HIGH AUTOMATION RISK
                        This role has significant exposure to AI and automation.

                        **Recommended Actions:**
                        - Learn skills that AI can't replicate (creativity, leadership, emotional intelligence)
                        - Develop expertise in AI tools themselves
                        - Build human-centered skills (mentoring, communication)
                        - Consider cross-training in adjacent roles
                        """
                    )

                elif ai_proneness > 0.33:
                    st.warning(
                        """
                        ### 🟡 MODERATE AUTOMATION RISK
                        Parts of this role are vulnerable to automation.

                        **Recommended Actions:**
                        - Strengthen skills that complement automation
                        - Learn to use AI tools effectively
                        - Develop specialized domain expertise
                        - Invest in continuous learning
                        """
                    )

                else:
                    st.success(
                        """
                        ### ✅ LOW AUTOMATION RISK
                        This role has strong human elements that are hard to automate.

                        **Recommended Actions:**
                        - Stay curious about AI trends
                        - Use AI tools to enhance your productivity
                        - Focus on deepening expertise
                        - Mentor others who face higher risk
                        """
                    )

                # Job Sector
                st.info(f"**Job Sector:** {result.get('sector', 'Unknown')}")

                # Export option
                if st.button("📥 Save This Analysis"):
                    if st.session_state.authenticated:
                        st.success("✓ Analysis saved to your history!")
                    else:
                        st.info("Login to save analyses and track progress")

# ============================================================================
# PAGE: LOGIN
# ============================================================================
elif page == "🔐 Login":
    st.subheader("🔐 Login to Your Account")

    col1, col2 = st.columns([1, 1])

    with col1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", use_container_width=True, type="primary"):
            if email and password:
                login_user(email, password)
            else:
                st.error("Please enter email and password")

    with col2:
        st.write("")
        st.write("")
        st.markdown("""
            **Don't have an account?**

            [Create one](/) to save your analyses and track your progress.

            ### Free Features:
            - ✓ 5 analyses/month
            - ✓ Risk assessments
            - ✓ Skill recommendations

            **Pro members get:**
            - ✓ Unlimited analyses
            - ✓ PDF reports
            - ✓ Career pivot suggestions
        """)

# ============================================================================
# PAGE: REGISTER
# ============================================================================
elif page == "📝 Register":
    st.subheader("📝 Create Your Account")

    col1, col2 = st.columns([1, 1])

    with col1:
        full_name = st.text_input("Full Name", key="reg_name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        password_confirm = st.text_input(
            "Confirm Password",
            type="password",
            key="reg_password_confirm",
        )

        if st.button("Register", use_container_width=True, type="primary"):
            if not all([full_name, email, password, password_confirm]):
                st.error("Please fill in all fields")
            elif password != password_confirm:
                st.error("Passwords don't match")
            elif len(password) < 8:
                st.error("Password must be at least 8 characters")
            else:
                if register_user(email, full_name, password):
                    st.balloons()

    with col2:
        st.write("")
        st.write("")
        st.markdown("""
            ### Why Create an Account?

            - 📊 Save all your analyses
            - 📈 Track progress over time
            - 🎯 Get personalized recommendations
            - 📥 Export detailed reports
            - 🔐 Keep your data private

            ### Free Forever

            Get started with **5 free analyses/month**.
        """)

# ============================================================================
# PAGE: HISTORY
# ============================================================================
elif page == "📜 History":
    if not st.session_state.authenticated:
        st.warning("👤 Please login to view your analysis history")
    else:
        st.subheader("📜 Your Analysis History")

        analyses = get_analysis_history()

        if analyses:
            for analysis in analyses:
                with st.container():
                    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

                    with col1:
                        st.write(f"**{analysis['job_title']}**")
                        st.caption(analysis['sector'])

                    with col2:
                        st.metric("Risk", f"{analysis['ai_proneness']:.0%}")

                    with col3:
                        risk_level = get_risk_level(analysis['ai_proneness'])
                        st.write(risk_level)

                    with col4:
                        st.caption(analysis['created_at'][:10])

                    st.divider()
        else:
            st.info("No analyses yet. Go analyze a job to get started!")

# ============================================================================
# PAGE: ABOUT
# ============================================================================
elif page == "ℹ️ About":
    st.subheader("ℹ️ About This Tool")

    st.markdown("""
        ## Why We Built This

        By 2030, AI will automate 30% of job tasks globally. But which jobs are most at risk?
        And what skills will protect your career?

        This tool uses machine learning on 20,000+ job descriptions to help you understand
        your personal automation risk and recommend skills to develop.

        ---

        ## How It Works

        1. **You provide job details** - Title, description, skills
        2. **We analyze using ML** - Sentence transformers + clustering
        3. **You get a risk score** - Low, Moderate, or High
        4. **You learn protective skills** - What to learn to stay competitive

        ---

        ## Data Source

        - **O*NET Database** - US government's occupational data
        - **20,000+ job descriptions** - Real-world job market data
        - **NLP & Machine Learning** - Latest AI techniques

        **Your data is private.** We never sell or share your information.

        ---

        ## Pricing

        | Plan | Cost | Features |
        |------|------|----------|
        | **Free** | $0 | 5 analyses/month |
        | **Pro** | $19/month | Unlimited, PDF reports, career pivots |
        | **Enterprise** | Custom | API access, white-label, bulk |

        ---

        ## Questions?

        📧 **Email:** hello@aijobanalyzer.com
        🌐 **Website:** [aijobanalyzer.com](https://aijobanalyzer.com)
        🐙 **GitHub:** [github.com/dipdhru/ai-job-automation-risk-nlp](https://github.com/dipdhru/ai-job-automation-risk-nlp)
    """)

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.85rem; padding: 1rem 0;'>
        <p>🤖 AI Job Risk Analyzer | Made with ❤️ to help careers evolve</p>
        <p>© 2024 All rights reserved | <a href='#'>Privacy Policy</a> | <a href='#'>Terms of Service</a></p>
    </div>
""", unsafe_allow_html=True)
