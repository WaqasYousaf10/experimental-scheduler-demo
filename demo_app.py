"""
Experimental Scheduler - Interactive Web Demo
Complete pre-loaded test data - No manual entry needed
Streamlit version - Runs in browser
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import random

# Page configuration
st.set_page_config(
    page_title="Experimental Scheduler - Demo",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .demo-badge {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: #FFA500;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        z-index: 999;
        font-size: 14px;
    }
    .feature-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .stat-card {
        background-color: #2E8B57;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        color: white;
    }
    .warning-card {
        background-color: #d13438;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        color: white;
    }
    .info-card {
        background-color: #3B8ED0;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .task-pending {
        border-left: 4px solid #FFA500;
        padding-left: 10px;
        margin: 5px 0;
    }
    .task-completed {
        border-left: 4px solid #2E8B57;
        padding-left: 10px;
        margin: 5px 0;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

# Demo badge
st.markdown('<div class="demo-badge">🔬 DEMO VERSION - Pre-loaded Data</div>', unsafe_allow_html=True)

# Title
st.title("📅 Experimental Scheduler")
st.caption("Plan, schedule, and track your PhD experiments - Complete pre-loaded demonstration")

# ============================================
# PRE-LOADED TEST DATA
# ============================================

# ---------- EXPERIMENT 1: Main Screening ----------
experiment_1 = {
    'id': 1,
    'name': 'Screening of Rice Genotypes for Combined Submergence + Iron Deficiency Tolerance',
    'type': 'Screening',
    'description': 'Testing 10 rice genotypes (FR13A, IR64, IR64-Sub1, Swarna, Swarna-Sub1, and 5 landraces) under control, Fe deficiency, submergence, and combined stress conditions',
    'start_date': datetime.now().strftime('%Y-%m-%d'),
    'end_date': (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'),
    'status': 'Active',
    'priority': 5,
    'progress': 35
}

# ---------- EXPERIMENT 2: Physiological Characterisation ----------
experiment_2 = {
    'id': 2,
    'name': 'Physiological Characterisation of Tolerant and Sensitive Genotypes',
    'type': 'Physiological',
    'description': 'Detailed physiological analysis of selected 3 tolerant and 3 sensitive genotypes',
    'start_date': (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
    'end_date': (datetime.now() + timedelta(days=100)).strftime('%Y-%m-%d'),
    'status': 'Planning',
    'priority': 4,
    'progress': 0
}

# ---------- EXPERIMENT 3: Molecular Analysis ----------
experiment_3 = {
    'id': 3,
    'name': 'Gene Expression Analysis of ERFVII and Fe Uptake Genes',
    'type': 'Molecular',
    'description': 'RT-qPCR analysis of SUB1A-1, OsIRT1, OsYSL15, OsIDS2, OsNAS1/2, OsADH1, OsPDC1 expression',
    'start_date': (datetime.now() + timedelta(days=110)).strftime('%Y-%m-%d'),
    'end_date': (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d'),
    'status': 'Planning',
    'priority': 5,
    'progress': 0
}

experiments = [experiment_1, experiment_2, experiment_3]

# ---------- PLANT BATCHES ----------
plant_batches = [
    {
        'id': 1,
        'experiment_id': 1,
        'name': 'Main Screening Batch',
        'species': 'Oryza sativa',
        'varieties': 'FR13A, IR64, IR64-Sub1, Swarna, Swarna-Sub1, 5 landraces',
        'seed_source': 'IRRI, Philippines',
        'sowing_date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
        'germination_date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
        'plant_count': 360,
        'status': 'Growing'
    },
    {
        'id': 2,
        'experiment_id': 1,
        'name': 'Replication Batch',
        'species': 'Oryza sativa',
        'varieties': 'FR13A, IR64, IR64-Sub1',
        'seed_source': 'IRRI, Philippines',
        'sowing_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
        'germination_date': (datetime.now() + timedelta(days=12)).strftime('%Y-%m-%d'),
        'plant_count': 180,
        'status': 'Planned'
    },
    {
        'id': 3,
        'experiment_id': 2,
        'name': 'Physiological Analysis Batch',
        'species': 'Oryza sativa',
        'varieties': '3 tolerant + 3 sensitive selected genotypes',
        'seed_source': 'IRRI, Philippines',
        'sowing_date': (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
        'germination_date': (datetime.now() + timedelta(days=55)).strftime('%Y-%m-%d'),
        'plant_count': 144,
        'status': 'Planned'
    }
]

# ---------- TASKS (20+ tasks) ----------
tasks = [
    # Experiment 1 tasks
    {'id': 1, 'experiment_id': 1, 'name': 'Sow seeds in trays', 'type': 'Sowing', 
     'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': True, 'notes': 'Use sterilised seeds, 10 seeds per pot'},
    {'id': 2, 'experiment_id': 1, 'name': 'Record germination count', 'type': 'Measurement', 
     'date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': True, 'notes': 'Count germinated seeds daily'},
    {'id': 3, 'experiment_id': 1, 'name': 'Transfer seedlings to hydroponics', 'type': 'Treatment', 
     'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': '2-leaf stage transfer'},
    {'id': 4, 'experiment_id': 1, 'name': 'Start Fe deficiency treatment', 'type': 'Treatment', 
     'date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': 'Remove Fe from nutrient solution'},
    {'id': 5, 'experiment_id': 1, 'name': 'Start submergence treatment', 'type': 'Treatment', 
     'date': (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': '10 cm water column'},
    {'id': 6, 'experiment_id': 1, 'name': 'Measure chlorophyll (SPAD)', 'type': 'Measurement', 
     'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': '3rd leaf measurement'},
    {'id': 7, 'experiment_id': 1, 'name': 'Harvest Day 14 samples', 'type': 'Harvest', 
     'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': 'Collect for RNA and enzyme assays'},
    {'id': 8, 'experiment_id': 1, 'name': 'Measure root length', 'type': 'Measurement', 
     'date': (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d'), 'priority': 3, 'completed': False, 'notes': 'Scan and measure with ImageJ'},
    {'id': 9, 'experiment_id': 1, 'name': 'Weigh biomass samples', 'type': 'Measurement', 
     'date': (datetime.now() + timedelta(days=16)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Fresh weight and dry weight'},
    {'id': 10, 'experiment_id': 1, 'name': 'De-submerge (recovery start)', 'type': 'Treatment', 
     'date': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Remove water'},
    {'id': 11, 'experiment_id': 1, 'name': 'Measure recovery survival', 'type': 'Measurement', 
     'date': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Count re-greening plants'},
    {'id': 12, 'experiment_id': 1, 'name': 'Final harvest', 'type': 'Harvest', 
     'date': (datetime.now() + timedelta(days=40)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': 'All remaining plants'},
    
    # Harvest Day 3 and 7 tasks (time course)
    {'id': 13, 'experiment_id': 1, 'name': 'Harvest Day 3 samples', 'type': 'Harvest', 
     'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Early stress response'},
    {'id': 14, 'experiment_id': 1, 'name': 'Harvest Day 7 samples', 'type': 'Harvest', 
     'date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Mid stress response'},
    
    # Experiment 2 tasks
    {'id': 15, 'experiment_id': 2, 'name': 'Prepare nutrient solutions', 'type': 'Preparation', 
     'date': (datetime.now() + timedelta(days=48)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'Control and Fe-deficient'},
    {'id': 16, 'experiment_id': 2, 'name': 'Sow seeds for physiology experiment', 'type': 'Sowing', 
     'date': (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': 'Selected genotypes'},
    {'id': 17, 'experiment_id': 2, 'name': 'Start treatments', 'type': 'Treatment', 
     'date': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d'), 'priority': 5, 'completed': False, 'notes': 'Apply stress treatments'},
    {'id': 18, 'experiment_id': 2, 'name': 'Measure antioxidant enzymes', 'type': 'Measurement', 
     'date': (datetime.now() + timedelta(days=74)).strftime('%Y-%m-%d'), 'priority': 4, 'completed': False, 'notes': 'SOD, CAT, APX, POD assays'},
]

# ---------- HARVEST SCHEDULE ----------
harvests = [
    {'id': 1, 'experiment_id': 1, 'day': 0, 'date': datetime.now().strftime('%Y-%m-%d'),
     'tissue': 'Baseline (whole seedlings)', 'samples': 30, 'storage': 'Liquid N2, -80°C',
     'parameters': 'RNA, enzyme activity, Fe content', 'completed': True},
    {'id': 2, 'experiment_id': 1, 'day': 3, 'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
     'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C',
     'parameters': 'RNA, enzyme activity', 'completed': False},
    {'id': 3, 'experiment_id': 1, 'day': 7, 'date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
     'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C',
     'parameters': 'RNA, enzyme activity, Fe content', 'completed': False},
    {'id': 4, 'experiment_id': 1, 'day': 14, 'date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
     'tissue': 'Leaves + Roots', 'samples': 45, 'storage': 'Liquid N2, -80°C, 70°C dried',
     'parameters': 'RNA, enzyme activity, Fe content, biomass', 'completed': False},
    {'id': 5, 'experiment_id': 1, 'day': 21, 'date': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'),
     'tissue': 'Leaves + Roots', 'samples': 30, 'storage': 'Liquid N2, -80°C',
     'parameters': 'RNA, enzyme activity', 'completed': False},
    {'id': 6, 'experiment_id': 1, 'day': 28, 'date': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d'),
     'tissue': 'Shoots only', 'samples': 30, 'storage': '70°C dried',
     'parameters': 'Biomass, Fe content', 'completed': False},
    
    # Experiment 2 harvests
    {'id': 7, 'experiment_id': 2, 'day': 0, 'date': (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
     'tissue': 'Baseline seedlings', 'samples': 18, 'storage': 'Liquid N2',
     'parameters': 'Enzyme activities, metabolites', 'completed': False},
    {'id': 8, 'experiment_id': 2, 'day': 14, 'date': (datetime.now() + timedelta(days=64)).strftime('%Y-%m-%d'),
     'tissue': 'Leaves + Roots', 'samples': 18, 'storage': '-80°C + 70°C',
     'parameters': 'All enzymes, biomass, Fe', 'completed': False},
]

# ---------- TREATMENT PLANNING ----------
treatments = [
    {'id': 1, 'experiment_id': 1, 'name': 'Control', 'type': 'Control', 
     'start_day': 0, 'end_day': 45, 'duration': 45, 
     'protocol': 'Normal nutrient solution (50 µM Fe-EDTA), drained conditions',
     'status': 'Active'},
    {'id': 2, 'experiment_id': 1, 'name': 'Iron Deficiency', 'type': 'Stress', 
     'start_day': 5, 'end_day': 45, 'duration': 40, 
     'protocol': 'Fe omitted from nutrient solution, renew every 3 days',
     'status': 'Active'},
    {'id': 3, 'experiment_id': 1, 'name': 'Submergence', 'type': 'Stress', 
     'start_day': 8, 'end_day': 28, 'duration': 20, 
     'protocol': '10 cm tap water column, renew every 2 days',
     'status': 'Active'},
    {'id': 4, 'experiment_id': 1, 'name': 'Combined Stress', 'type': 'Stress', 
     'start_day': 5, 'end_day': 45, 'duration': 40, 
     'protocol': 'Fe deficiency + Submergence',
     'status': 'Active'},
    {'id': 5, 'experiment_id': 1, 'name': 'Recovery', 'type': 'Treatment', 
     'start_day': 21, 'end_day': 45, 'duration': 24, 
     'protocol': 'De-submerge, return to Fe-sufficient conditions',
     'status': 'Planned'},
    
    # Experiment 4: Pharmacological treatments
    {'id': 6, 'experiment_id': 3, 'name': 'ACC (50 µM)', 'type': 'Chemical', 
     'start_day': 1, 'end_day': 7, 'duration': 7, 
     'protocol': 'Add ACC to nutrient solution daily (ethylene precursor)',
     'status': 'Planning'},
    {'id': 7, 'experiment_id': 3, 'name': 'AVG (10 µM)', 'type': 'Chemical', 
     'start_day': 1, 'end_day': 7, 'duration': 7, 
     'protocol': 'Add AVG to nutrient solution daily (ethylene biosynthesis inhibitor)',
     'status': 'Planning'},
    {'id': 8, 'experiment_id': 3, 'name': 'STS (10 µM)', 'type': 'Chemical', 
     'start_day': 1, 'end_day': 7, 'duration': 7, 
     'protocol': 'Add STS to nutrient solution daily (ethylene perception inhibitor)',
     'status': 'Planning'},
]

# ---------- LAB SUPPLIES INVENTORY ----------
supplies = [
    {'name': 'MS Basal Salts', 'category': 'Media', 'quantity': 500, 'unit': 'g', 'threshold': 100, 'location': 'Cold room', 'status': 'OK'},
    {'name': 'Sucrose', 'category': 'Media', 'quantity': 1000, 'unit': 'g', 'threshold': 200, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Agar', 'category': 'Media', 'quantity': 250, 'unit': 'g', 'threshold': 50, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Fe-EDTA', 'category': 'Chemicals', 'quantity': 3, 'unit': 'g', 'threshold': 5, 'location': 'Dark cabinet', 'status': 'LOW'},
    {'name': '2,2\'-bipyridyl', 'category': 'Chemicals', 'quantity': 0.5, 'unit': 'g', 'threshold': 1, 'location': 'Dark cabinet', 'status': 'LOW'},
    {'name': 'ACC', 'category': 'Chemicals', 'quantity': 15, 'unit': 'mg', 'threshold': 20, 'location': '-20°C', 'status': 'LOW'},
    {'name': 'AVG', 'category': 'Chemicals', 'quantity': 25, 'unit': 'mg', 'threshold': 10, 'location': '-20°C', 'status': 'OK'},
    {'name': 'AgNO₃', 'category': 'Chemicals', 'quantity': 8, 'unit': 'g', 'threshold': 2, 'location': 'Dark cabinet', 'status': 'OK'},
    {'name': 'RNA Extraction Kit', 'category': 'Kits', 'quantity': 1, 'unit': 'kit', 'threshold': 1, 'location': '-20°C', 'status': 'LOW'},
    {'name': 'cDNA Synthesis Kit', 'category': 'Kits', 'quantity': 1, 'unit': 'kit', 'threshold': 1, 'location': '-20°C', 'status': 'LOW'},
    {'name': 'SYBR Green Master Mix', 'category': 'Kits', 'quantity': 1, 'unit': 'pack', 'threshold': 1, 'location': '-20°C', 'status': 'LOW'},
    {'name': '96-well plates', 'category': 'Plastics', 'quantity': 2, 'unit': 'box', 'threshold': 2, 'location': 'Room temp', 'status': 'LOW'},
    {'name': '1.5 mL tubes', 'category': 'Plastics', 'quantity': 3, 'unit': 'bag', 'threshold': 1, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Pipette tips (10 µL)', 'category': 'Plastics', 'quantity': 5, 'unit': 'box', 'threshold': 2, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Pipette tips (200 µL)', 'category': 'Plastics', 'quantity': 3, 'unit': 'box', 'threshold': 2, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Nitric Acid (65%)', 'category': 'Chemicals', 'quantity': 300, 'unit': 'mL', 'threshold': 100, 'location': 'Acid cabinet', 'status': 'OK'},
    {'name': 'Hydrogen Peroxide (30%)', 'category': 'Chemicals', 'quantity': 150, 'unit': 'mL', 'threshold': 50, 'location': 'Chemical cabinet', 'status': 'OK'},
    {'name': 'NBT (Nitroblue tetrazolium)', 'category': 'Chemicals', 'quantity': 3, 'unit': 'g', 'threshold': 1, 'location': 'Dark cabinet', 'status': 'OK'},
    {'name': 'Guaiacol', 'category': 'Chemicals', 'quantity': 80, 'unit': 'mL', 'threshold': 20, 'location': 'Room temp', 'status': 'OK'},
    {'name': 'Bradford Reagent', 'category': 'Chemicals', 'quantity': 300, 'unit': 'mL', 'threshold': 100, 'location': '4°C', 'status': 'OK'},
]

# ---------- GANTT CHART DATA ----------
gantt_data = [
    {'task': 'Experiment Setup', 'start': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'), 'status': 'Completed'},
    {'task': 'Fe Deficiency Treatment', 'start': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'), 'status': 'Active'},
    {'task': 'Submergence Treatment', 'start': (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d'), 'status': 'Active'},
    {'task': 'Harvest Day 3', 'start': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'), 'status': 'Pending'},
    {'task': 'Harvest Day 7', 'start': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'), 'status': 'Pending'},
    {'task': 'Harvest Day 14', 'start': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'), 'status': 'Pending'},
    {'task': 'Recovery Phase', 'start': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'), 'status': 'Pending'},
    {'task': 'Final Harvest', 'start': (datetime.now() + timedelta(days=40)).strftime('%Y-%m-%d'), 
     'end': (datetime.now() + timedelta(days=40)).strftime('%Y-%m-%d'), 'status': 'Pending'},
]

# ---------- STATISTICS ----------
def calculate_stats():
    total_tasks = len([t for t in tasks if t['experiment_id'] == 1])
    completed_tasks = len([t for t in tasks if t['experiment_id'] == 1 and t['completed']])
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    total_harvests = len([h for h in harvests if h['experiment_id'] == 1])
    completed_harvests = len([h for h in harvests if h['experiment_id'] == 1 and h['completed']])
    harvest_progress = (completed_harvests / total_harvests * 100) if total_harvests > 0 else 0
    
    low_stock = len([s for s in supplies if s['status'] == 'LOW'])
    
    return {
        'completion_rate': completion_rate,
        'harvest_progress': harvest_progress,
        'low_stock': low_stock,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'total_harvests': total_harvests,
        'completed_harvests': completed_harvests
    }

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.image("https://img.icons8.com/color/96/calendar--v1.png", width=80)
    st.markdown("## 📅 Experimental Scheduler")
    st.markdown("---")
    
    # Demo info
    st.markdown("### ℹ️ Demo Information")
    st.info("""
    This demo comes with **pre-loaded test data**:
    - 3 experiments
    - 3 plant batches
    - 18 tasks
    - 8 harvest time points
    - 8 treatments
    - 20 lab supplies
    - Complete Gantt chart
    
    **No manual entry needed!**
    """)
    
    st.markdown("---")
    
    # Quick stats
    stats = calculate_stats()
    st.markdown("### 📊 Quick Stats")
    st.metric("Task Completion", f"{stats['completion_rate']:.0f}%", 
              delta=f"{stats['completed_tasks']}/{stats['total_tasks']}")
    st.metric("Harvest Progress", f"{stats['harvest_progress']:.0f}%",
              delta=f"{stats['completed_harvests']}/{stats['total_harvests']}")
    st.metric("Low Stock Items", stats['low_stock'], delta="⚠️ Order soon" if stats['low_stock'] > 0 else None)
    
    st.markdown("---")
    
    # Purchase CTA
    st.markdown("### 🛒 Get Full Version")
    st.markdown("**$89** one-time license")
    if st.button("💳 Purchase Now", use_container_width=True):
        st.info("Contact: your-email@example.com")
    
    st.markdown("---")
    st.caption("© 2024 Experimental Scheduler Demo")

# ============================================
# MAIN CONTENT TABS
# ============================================

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Dashboard", "📋 Experiments", "🌾 Plant Batches", "✅ Tasks", 
    "🌽 Harvest Schedule", "💊 Treatments", "📦 Supplies"
])

# ==================== TAB 1: DASHBOARD ====================
with tab1:
    st.header("Experiment Dashboard")
    
    # Stats cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <h3>🎯 {stats['completion_rate']:.0f}%</h3>
            <p>Task Completion</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <h3>🌾 {stats['harvest_progress']:.0f}%</h3>
            <p>Harvest Progress</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <h3>📦 {stats['low_stock']}</h3>
            <p>Low Stock Alerts</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <h3>🔬 {len([e for e in experiments if e['status'] == 'Active'])}</h3>
            <p>Active Experiments</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress bars
    st.subheader("Overall Progress")
    st.progress(stats['completion_rate'] / 100)
    
    # Current experiment details
    st.subheader("📌 Current Active Experiment")
    active_exp = experiment_1
    st.markdown(f"""
    <div class="feature-card">
        <h3>{active_exp['name']}</h3>
        <p><strong>Type:</strong> {active_exp['type']} | <strong>Priority:</strong> {'⭐' * active_exp['priority']}</p>
        <p><strong>Period:</strong> {active_exp['start_date']} → {active_exp['end_date']}</p>
        <p><strong>Description:</strong> {active_exp['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upcoming tasks
    st.subheader("📋 Upcoming Tasks (Next 7 Days)")
    today = datetime.now()
    upcoming_tasks = [t for t in tasks if not t['completed'] and 
                      datetime.strptime(t['date'], '%Y-%m-%d') >= today and
                      datetime.strptime(t['date'], '%Y-%m-%d') <= today + timedelta(days=7)]
    upcoming_tasks.sort(key=lambda x: x['date'])
    
    if upcoming_tasks:
        for task in upcoming_tasks[:5]:
            days_left = (datetime.strptime(task['date'], '%Y-%m-%d') - today).days
            st.markdown(f"""
            <div class="task-pending">
                <strong>{task['name']}</strong><br>
                📅 {task['date']} ({days_left} days) | ⭐ {task['priority']} | Type: {task['type']}
                <br><small>{task.get('notes', '')}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("No upcoming tasks in the next 7 days!")
    
    # Low stock warning
    low_stock_items = [s for s in supplies if s['status'] == 'LOW']
    if low_stock_items:
        st.warning("⚠️ **Low Stock Alert!** Please reorder the following items:")
        for item in low_stock_items:
            st.write(f"- **{item['name']}**: {item['quantity']} {item['unit']} remaining (min: {item['threshold']} {item['unit']})")

# ==================== TAB 2: EXPERIMENTS ====================
with tab2:
    st.header("All Experiments")
    
    for exp in experiments:
        with st.expander(f"📌 {exp['name']}", expanded=(exp['status'] == 'Active')):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                **Type:** {exp['type']}  
                **Status:** {exp['status']}  
                **Priority:** {'⭐' * exp['priority']}  
                **Period:** {exp['start_date']} → {exp['end_date']}  
                **Description:** {exp['description']}
                """)
            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <h3>{exp['progress']}%</h3>
                    <p>Progress</p>
                </div>
                """, unsafe_allow_html=True)
            st.progress(exp['progress'] / 100)

# ==================== TAB 3: PLANT BATCHES ====================
with tab3:
    st.header("Plant Batches")
    
    for batch in plant_batches:
        with st.expander(f"🌱 {batch['name']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                **Species:** {batch['species']}  
                **Varieties:** {batch['varieties']}  
                **Seed Source:** {batch['seed_source']}  
                **Sowing Date:** {batch['sowing_date']}
                """)
            with col2:
                st.markdown(f"""
                **Germination Date:** {batch['germination_date']}  
                **Plant Count:** {batch['plant_count']} plants  
                **Status:** {batch['status']}
                """)
    
    # Batch summary table
    st.subheader("Batches Summary")
    batch_df = pd.DataFrame(plant_batches)[['name', 'species', 'plant_count', 'status', 'sowing_date']]
    batch_df.columns = ['Batch Name', 'Species', 'Plants', 'Status', 'Sowing Date']
    st.dataframe(batch_df, use_container_width=True)

# ==================== TAB 4: TASKS ====================
with tab4:
    st.header("Task Management")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_exp = st.selectbox("Experiment", ["All", experiment_1['name'], experiment_2['name'], experiment_3['name']])
    with col2:
        filter_status = st.selectbox("Status", ["All", "Pending", "Completed"])
    with col3:
        filter_priority = st.selectbox("Priority", ["All", "5 (Highest)", "4", "3", "2", "1 (Lowest)"])
    
    # Filter tasks
    filtered_tasks = tasks
    if filter_exp != "All":
        exp_map = {experiment_1['name']: 1, experiment_2['name']: 2, experiment_3['name']: 3}
        filtered_tasks = [t for t in filtered_tasks if t['experiment_id'] == exp_map.get(filter_exp)]
    if filter_status != "All":
        filtered_tasks = [t for t in filtered_tasks if (t['completed'] and filter_status == "Completed") or (not t['completed'] and filter_status == "Pending")]
    if filter_priority != "All":
        priority_val = int(filter_priority.split()[0])
        filtered_tasks = [t for t in filtered_tasks if t['priority'] == priority_val]
    
    # Display tasks
    for task in filtered_tasks:
        task_class = "task-completed" if task['completed'] else "task-pending"
        checkmark = "✅" if task['completed'] else "⏳"
        st.markdown(f"""
        <div class="{task_class}">
            <strong>{checkmark} {task['name']}</strong><br>
            📅 {task['date']} | 🏷️ {task['type']} | ⭐ {task['priority']}<br>
            <small>{task.get('notes', '')}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Task statistics
    st.subheader("Task Statistics")
    task_df = pd.DataFrame(tasks)
    if not task_df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tasks", len(tasks))
        with col2:
            st.metric("Completed", len([t for t in tasks if t['completed']]))
        with col3:
            st.metric("Pending", len([t for t in tasks if not t['completed']]))

# ==================== TAB 5: HARVEST SCHEDULE ====================
with tab5:
    st.header("Harvest Schedule")
    
    # Harvest timeline visualization
    st.subheader("📊 Harvest Timeline")
    harvest_df = pd.DataFrame(harvests)
    
    if not harvest_df.empty:
        # Create timeline chart
        fig = go.Figure()
        
        for _, harvest in harvest_df.iterrows():
            color = '#2E8B57' if harvest['completed'] else '#FFA500'
            fig.add_trace(go.Scatter(
                x=[harvest['date']],
                y=[harvest['tissue']],
                mode='markers+text',
                marker=dict(size=25, color=color, symbol='circle'),
                text=[f"Day {harvest['day']}"],
                textposition="top center",
                name=f"Day {harvest['day']}"
            ))
        
        fig.update_layout(
            title="Harvest Time Points",
            xaxis_title="Date",
            yaxis_title="Tissue Type",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Harvest table
        st.subheader("📋 Harvest Details")
        display_df = harvest_df[['day', 'date', 'tissue', 'samples', 'storage', 'parameters', 'completed']]
        display_df.columns = ['Day', 'Date', 'Tissue', 'Samples', 'Storage', 'Parameters', 'Completed']
        display_df['Completed'] = display_df['Completed'].map({True: '✅ Yes', False: '⏳ No'})
        st.dataframe(display_df, use_container_width=True)
        
        # Sample collection checklist
        st.subheader("📝 Sample Collection Checklist")
        for harvest in harvests:
            if not harvest['completed']:
                st.checkbox(f"**Day {harvest['day']}** - {harvest['tissue']}: Collect {harvest['samples']} samples → Store in {harvest['storage']}")

# ==================== TAB 6: TREATMENTS ====================
with tab6:
    st.header("Treatment Planning")
    
    for treatment in treatments:
        with st.expander(f"💊 {treatment['name']} ({treatment['type']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                **Type:** {treatment['type']}  
                **Start Day:** Day {treatment['start_day']}  
                **End Day:** Day {treatment['end_day']}  
                **Duration:** {treatment['duration']} days
                """)
            with col2:
                st.markdown(f"""
                **Status:** {treatment['status']}  
                **Protocol:** {treatment['protocol']}
                """)
    
    # Treatment schedule timeline
    st.subheader("📊 Treatment Schedule Timeline")
    treat_df = pd.DataFrame(treatments)
    if not treat_df.empty:
        fig = go.Figure()
        
        for _, treat in treat_df.iterrows():
            fig.add_trace(go.Bar(
                x=[treat['duration']],
                y=[treat['name']],
                orientation='h',
                marker_color='#2E8B57' if treat['status'] == 'Active' else '#FFA500',
                text=f"Day {treat['start_day']} → Day {treat['end_day']}",
                textposition='outside',
                name=treat['name']
            ))
        
        fig.update_layout(
            title="Treatment Timeline",
            xaxis_title="Duration (days)",
            yaxis_title="Treatment",
            height=400,
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== TAB 7: SUPPLIES ====================
with tab7:
    st.header("Lab Supplies Inventory")
    
    # Low stock warning
    low_stock_items = [s for s in supplies if s['status'] == 'LOW']
    if low_stock_items:
        st.warning("⚠️ **URGENT: Low Stock Alert!**")
        for item in low_stock_items:
            st.markdown(f"""
            <div class="warning-card">
                <strong>{item['name']}</strong>: {item['quantity']} {item['unit']} remaining 
                (Minimum threshold: {item['threshold']} {item['unit']})
            </div>
            """, unsafe_allow_html=True)
    
    # Supplies table with categories
    st.subheader("📦 Complete Inventory")
    
    categories = supplies_df['category'].unique() if 'supplies_df' in dir() else list(set(s['category'] for s in supplies))
    for category in categories:
        st.markdown(f"#### 📁 {category}")
        cat_supplies = [s for s in supplies if s['category'] == category]
        cat_df = pd.DataFrame(cat_supplies)
        cat_df = cat_df[['name', 'quantity', 'unit', 'threshold', 'location', 'status']]
        cat_df.columns = ['Item', 'Quantity', 'Unit', 'Min Threshold', 'Location', 'Status']
        
        # Color code status
        def color_status(val):
            if val == 'LOW':
                return 'background-color: #d13438; color: white'
            return ''
        
        st.dataframe(cat_df.style.applymap(color_status, subset=['Status']), use_container_width=True)
    
    # Reorder form
    st.subheader("📝 Reorder Form (Demo)")
    st.caption("Full version allows direct ordering from suppliers")
    reorder_item = st.selectbox("Select item to reorder", [s['name'] for s in low_stock_items] if low_stock_items else ["No low stock items"])
    reorder_qty = st.number_input("Quantity to order", min_value=1, value=100)
    if st.button("📧 Send Reorder Request (Demo)"):
        st.success(f"Reorder request for {reorder_qty} units of {reorder_item} sent to supplier (Demo)")

# ============================================
# FOOTER
# ============================================

st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px;">
    <strong>Experimental Scheduler Demo v1.0</strong><br>
    All data pre-loaded for demonstration | No manual entry required<br>
    <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">Contact Support</a>
    <br><br>
    🔒 This is a demo version. <a href="#">Purchase full version ($89)</a> for unlimited experiments, Excel export, and priority support.
</div>
""", unsafe_allow_html=True)