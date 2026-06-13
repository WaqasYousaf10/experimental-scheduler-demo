"""
Experimental Scheduler - Simplified Demo (No Plotly)
Works immediately - No additional dependencies
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Experimental Scheduler - Demo",
    page_icon="📅",
    layout="wide"
)

# Demo badge
st.markdown("""
<div style="position: fixed; top: 10px; right: 10px; background-color: #FFA500; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; z-index: 999;">
    🔬 DEMO VERSION
</div>
""", unsafe_allow_html=True)

# Title
st.title("📅 Experimental Scheduler")
st.caption("Plan, schedule, and track your PhD experiments - Complete pre-loaded demonstration")

# ============================================
# PRE-LOADED TEST DATA (No manual entry needed)
# ============================================

# Experiments
experiments = [
    {'name': 'Screening of Rice Genotypes for Combined Stress Tolerance', 'status': 'Active', 'progress': 35, 'priority': 5},
    {'name': 'Physiological Characterisation of Tolerant Genotypes', 'status': 'Planning', 'progress': 0, 'priority': 4},
    {'name': 'Gene Expression Analysis (RT-qPCR)', 'status': 'Planning', 'progress': 0, 'priority': 5},
]

# Tasks
tasks = [
    {'name': '✅ Sow seeds in trays', 'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'), 'completed': True, 'priority': 5, 'type': 'Sowing'},
    {'name': '✅ Record germination count', 'date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), 'completed': True, 'priority': 4, 'type': 'Measurement'},
    {'name': '⏳ Transfer seedlings to hydroponics', 'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 5, 'type': 'Treatment'},
    {'name': '⏳ Start Fe deficiency treatment', 'date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 5, 'type': 'Treatment'},
    {'name': '⏳ Start submergence treatment', 'date': (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 5, 'type': 'Treatment'},
    {'name': '⏳ Measure chlorophyll (SPAD)', 'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 4, 'type': 'Measurement'},
    {'name': '⏳ Harvest Day 14 samples', 'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 5, 'type': 'Harvest'},
    {'name': '⏳ Measure root length', 'date': (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 3, 'type': 'Measurement'},
    {'name': '⏳ De-submerge (recovery start)', 'date': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 4, 'type': 'Treatment'},
    {'name': '⏳ Final harvest', 'date': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d'), 'completed': False, 'priority': 5, 'type': 'Harvest'},
]

# Plant Batches
plant_batches = [
    {'name': 'Main Screening Batch', 'species': 'Oryza sativa', 'varieties': 'FR13A, IR64, IR64-Sub1, Swarna, Swarna-Sub1, 5 landraces', 'plants': 360, 'status': 'Growing'},
    {'name': 'Replication Batch', 'species': 'Oryza sativa', 'varieties': 'FR13A, IR64, IR64-Sub1', 'plants': 180, 'status': 'Planned'},
    {'name': 'Physiology Batch', 'species': 'Oryza sativa', 'varieties': '3 tolerant + 3 sensitive', 'plants': 144, 'status': 'Planned'},
]

# Harvest Schedule
harvests = [
    {'day': 0, 'date': datetime.now().strftime('%Y-%m-%d'), 'tissue': 'Baseline', 'samples': 30, 'storage': 'Liquid N2, -80°C', 'completed': True},
    {'day': 3, 'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C', 'completed': False},
    {'day': 7, 'date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'), 'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C', 'completed': False},
    {'day': 14, 'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'tissue': 'Leaves + Roots', 'samples': 45, 'storage': 'Liquid N2, -80°C, 70°C', 'completed': False},
    {'day': 21, 'date': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'), 'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C', 'completed': False},
    {'day': 28, 'date': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d'), 'tissue': 'Shoots', 'samples': 30, 'storage': '70°C dried', 'completed': False},
]

# Treatments
treatments = [
    {'name': 'Control', 'type': 'Control', 'start_day': 0, 'end_day': 45, 'status': 'Active'},
    {'name': 'Iron Deficiency', 'type': 'Stress', 'start_day': 5, 'end_day': 45, 'status': 'Active'},
    {'name': 'Submergence', 'type': 'Stress', 'start_day': 8, 'end_day': 28, 'status': 'Active'},
    {'name': 'Combined Stress', 'type': 'Stress', 'start_day': 5, 'end_day': 45, 'status': 'Active'},
    {'name': 'Recovery', 'type': 'Treatment', 'start_day': 21, 'end_day': 45, 'status': 'Planned'},
]

# Lab Supplies
supplies = [
    {'name': 'Fe-EDTA', 'quantity': 3, 'unit': 'g', 'threshold': 5, 'status': '⚠️ LOW', 'category': 'Chemicals'},
    {'name': 'RNA Extraction Kit', 'quantity': 1, 'unit': 'kit', 'threshold': 1, 'status': '⚠️ LOW', 'category': 'Kits'},
    {'name': '2,2\'-bipyridyl', 'quantity': 0.5, 'unit': 'g', 'threshold': 1, 'status': '⚠️ LOW', 'category': 'Chemicals'},
    {'name': 'MS Basal Salts', 'quantity': 500, 'unit': 'g', 'threshold': 100, 'status': '✅ OK', 'category': 'Media'},
    {'name': 'Sucrose', 'quantity': 1000, 'unit': 'g', 'threshold': 200, 'status': '✅ OK', 'category': 'Media'},
    {'name': '96-well plates', 'quantity': 2, 'unit': 'box', 'threshold': 2, 'status': '⚠️ LOW', 'category': 'Plastics'},
    {'name': 'SYBR Green Master Mix', 'quantity': 1, 'unit': 'pack', 'threshold': 1, 'status': '⚠️ LOW', 'category': 'Kits'},
]

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.image("https://img.icons8.com/color/96/calendar--v1.png", width=80)
    st.markdown("## 📅 Experimental Scheduler")
    st.markdown("---")
    
    # Stats
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t['completed']])
    pending_tasks = total_tasks - completed_tasks
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    
    st.progress(completed_tasks / total_tasks if total_tasks > 0 else 0)
    
    st.markdown("---")
    
    # Low stock warning
    low_stock = [s for s in supplies if '⚠️' in s['status']]
    if low_stock:
        st.warning(f"⚠️ {len(low_stock)} items low in stock")
    
    st.markdown("---")
    
    # Purchase
    st.markdown("### 🛒 Get Full Version")
    st.markdown("**$89** one-time license")
    if st.button("💳 Purchase Now", use_container_width=True):
        st.info("Contact: waqasyousaf2012@gmail.com")
    
    st.markdown("---")
    st.caption("© 2024 Experimental Scheduler Demo")

# ============================================
# MAIN TABS
# ============================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Dashboard", "📋 Experiments", "🌾 Plant Batches", 
    "✅ Tasks", "🌽 Harvest Schedule", "📦 Supplies"
])

# ==================== TAB 1: DASHBOARD ====================
with tab1:
    st.header("Experiment Dashboard")
    
    # Stats cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Experiments", len([e for e in experiments if e['status'] == 'Active']))
    with col2:
        st.metric("Total Tasks", total_tasks)
    with col3:
        st.metric("Completed Tasks", completed_tasks)
    with col4:
        st.metric("Pending Tasks", pending_tasks)
    
    # Current experiment
    st.subheader("📌 Current Active Experiment")
    active_exp = experiments[0]
    st.markdown(f"""
    **{active_exp['name']}**  
    Status: {active_exp['status']} | Priority: {'⭐' * active_exp['priority']}  
    Progress: {active_exp['progress']}%
    """)
    st.progress(active_exp['progress'] / 100)
    
    # Upcoming tasks
    st.subheader("📋 Upcoming Tasks (Next 7 Days)")
    today = datetime.now()
    upcoming = []
    for task in tasks:
        if not task['completed']:
            try:
                task_date = datetime.strptime(task['date'], '%Y-%m-%d')
                if task_date >= today and task_date <= today + timedelta(days=7):
                    upcoming.append(task)
            except:
                pass
    
    if upcoming:
        for task in upcoming[:5]:
            days_left = (datetime.strptime(task['date'], '%Y-%m-%d') - today).days
            st.write(f"• **{task['name']}** - Due: {task['date']} ({days_left} days) - Priority: {'⭐' * task['priority']}")
    else:
        st.success("No upcoming tasks in the next 7 days!")
    
    # Low stock alert
    if low_stock:
        st.warning("⚠️ **Low Stock Alert!**")
        for item in low_stock[:3]:
            st.write(f"  - {item['name']}: {item['quantity']} {item['unit']} remaining")

# ==================== TAB 2: EXPERIMENTS ====================
with tab2:
    st.header("All Experiments")
    
    for exp in experiments:
        with st.expander(f"📌 {exp['name']}", expanded=(exp['status'] == 'Active')):
            st.markdown(f"""
            **Status:** {exp['status']}  
            **Priority:** {'⭐' * exp['priority']}  
            **Progress:** {exp['progress']}%
            """)
            st.progress(exp['progress'] / 100)

# ==================== TAB 3: PLANT BATCHES ====================
with tab3:
    st.header("Plant Batches")
    
    batch_df = pd.DataFrame(plant_batches)
    st.dataframe(batch_df, use_container_width=True)
    
    # Summary
    total_plants = sum(b['plants'] for b in plant_batches)
    st.info(f"📊 Total plants across all batches: **{total_plants}**")

# ==================== TAB 4: TASKS ====================
with tab4:
    st.header("Task Management")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        filter_status = st.selectbox("Show", ["All Tasks", "Pending Only", "Completed Only"])
    with col2:
        filter_priority = st.selectbox("Priority", ["All", "High (5⭐)", "Medium (3-4⭐)", "Low (1-2⭐)"])
    
    # Display tasks
    for task in tasks:
        show = True
        if filter_status == "Pending Only" and task['completed']:
            show = False
        if filter_status == "Completed Only" and not task['completed']:
            show = False
        if filter_priority == "High (5⭐)" and task['priority'] != 5:
            show = False
        if filter_priority == "Medium (3-4⭐)" and task['priority'] not in [3, 4]:
            show = False
        if filter_priority == "Low (1-2⭐)" and task['priority'] not in [1, 2]:
            show = False
        
        if show:
            if task['completed']:
                st.markdown(f"✅ ~~**{task['name']}**~~ - {task['date']} (Priority: {'⭐' * task['priority']})")
            else:
                st.markdown(f"⏳ **{task['name']}** - {task['date']} (Priority: {'⭐' * task['priority']}) - Type: {task['type']}")

# ==================== TAB 5: HARVEST SCHEDULE ====================
with tab5:
    st.header("Harvest Schedule")
    
    harvest_df = pd.DataFrame(harvests)
    harvest_df['Completed'] = harvest_df['completed'].map({True: '✅ Yes', False: '⏳ No'})
    harvest_df_display = harvest_df[['day', 'date', 'tissue', 'samples', 'storage', 'Completed']]
    harvest_df_display.columns = ['Day', 'Date', 'Tissue', 'Samples', 'Storage', 'Completed']
    st.dataframe(harvest_df_display, use_container_width=True)
    
    # Checklist
    st.subheader("📝 Sample Collection Checklist")
    for harvest in harvests:
        if not harvest['completed']:
            st.checkbox(f"**Day {harvest['day']}** - {harvest['tissue']}: Collect {harvest['samples']} samples → Store in {harvest['storage']}")

# ==================== TAB 6: SUPPLIES ====================
with tab6:
    st.header("Lab Supplies Inventory")
    
    # Group by category
    categories = list(set(s['category'] for s in supplies))
    for category in categories:
        st.subheader(f"📁 {category}")
        cat_supplies = [s for s in supplies if s['category'] == category]
        for supply in cat_supplies:
            if '⚠️' in supply['status']:
                st.warning(f"**{supply['name']}**: {supply['quantity']} {supply['unit']} (Min: {supply['threshold']} {supply['unit']})")
            else:
                st.write(f"✅ **{supply['name']}**: {supply['quantity']} {supply['unit']}")

# ============================================
# FOOTER
# ============================================

st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px;">
    <strong>Experimental Scheduler Demo v1.0</strong><br>
    All data pre-loaded for demonstration | No manual entry required<br>
    🔒 <a href="#">Purchase full version ($89)</a> for unlimited experiments, Excel export, and priority support.
</div>
""", unsafe_allow_html=True)