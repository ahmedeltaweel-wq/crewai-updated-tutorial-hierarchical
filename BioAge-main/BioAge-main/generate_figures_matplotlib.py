import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap

# Set global font and style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.style.use('seaborn-v0_8-whitegrid')

def create_evolution_timeline():
    """Generates the Evolution of Wearable Insurance Programs Timeline"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data
    eras = [
        {"year": 2015, "title": "Basic Step Counting", "desc": "Simple discounts for 10,000 steps/day", "color": "#3498db"},
        {"year": 2018, "title": "Multi-Metric Approach", "desc": "Added heart rate, sleep, nutrition tracking", "color": "#2ecc71"},
        {"year": 2020, "title": "AI-Powered Analysis", "desc": "ML for fraud detection & personalized health", "color": "#e67e22"},
        {"year": 2023, "title": "Biological Age Integration", "desc": "Composite biomarker scoring (PhenoAge)", "color": "#9b59b6"},
        {"year": 2024, "title": "Predictive Health Models", "desc": "Real-time risk prediction & interventions", "color": "#f1c40f"}
    ]
    
    # Setup axis
    ax.set_xlim(2014, 2026)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Draw central line
    ax.plot([2015, 2024], [3, 3], color='#7f8c8d', linewidth=3, zorder=1)
    
    for i, era in enumerate(eras):
        year = era['year']
        
        # Draw node
        circle = plt.Circle((year, 3), 0.3, color=era['color'], zorder=2)
        ax.add_patch(circle)
        
        # Year label
        ax.text(year, 3, str(year), ha='center', va='center', color='white', fontweight='bold', zorder=3)
        
        # Alternating positions for text
        y_pos = 1.5 if i % 2 == 0 else 4.0
        va = 'top' if i % 2 == 0 else 'bottom'
        
        # Connector line
        ax.plot([year, year], [3, y_pos], color=era['color'], linestyle='--', linewidth=1.5, zorder=1)
        
        # Box for text
        box_y = y_pos if i % 2 != 0 else y_pos - 0.5
        box = patches.FancyBboxPatch((year - 0.8, box_y), 1.6, 1.2, boxstyle="round,pad=0.1", 
                                     linewidth=2, edgecolor=era['color'], facecolor='white', zorder=2)
        ax.add_patch(box)
        
        # Text
        text_y = box_y + 0.9
        ax.text(year, text_y, era['title'], ha='center', va='top', fontweight='bold', color=era['color'], fontsize=10, wrap=True)
        
        wrapped_desc = "\n".join(textwrap.wrap(era['desc'], width=20))
        ax.text(year, text_y - 0.3, wrapped_desc, ha='center', va='top', color='#2c3e50', fontsize=9)

    plt.title("Evolution of Wearable Insurance Programs", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('figures/Figure_7.2_Evolution_Timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Figure_7.2_Evolution_Timeline.png")

def create_egypt_opportunity():
    """Generates the Egyptian Market Opportunity Info-graphic"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, "EGYPTIAN MARKET OPPORTUNITY ANALYSIS", ha='center', va='center', fontsize=18, fontweight='bold', color='#c0392b')
    
    opportunities = [
        {"title": "LOW INSURANCE PENETRATION", "stats": "0.9% GDP → Massive Growth Potential", "desc": "Interactive products could boost penetration 3-5x", "color": "#e74c3c", "y": 8},
        {"title": "YOUNG POPULATION", "stats": "Median Age: 24 Years", "desc": "Tech-savvy demographics ideal for wearables", "color": "#3498db", "y": 6.5},
        {"title": "HIGH CHRONIC DISEASE BURDEN", "stats": "Diabetes: 20.9% Prevalence", "desc": "Preventive incentives could significantly reduce burden", "color": "#9b59b6", "y": 5},
        {"title": "REGULATORY MODERNIZATION", "stats": "New FinTech & InsurTech Laws", "desc": "FRA modernizing framework & Data Protection Law", "color": "#2ecc71", "y": 3.5},
        {"title": "MOBILE-FIRST ECONOMY", "stats": "76% Smartphone Adoption", "desc": "Strong digital payment infra (Fawry, etc.)", "color": "#f39c12", "y": 2}
    ]
    
    for item in opportunities:
        # Background box
        # rect = patches.FancyBboxPatch((0.5, item['y'] - 1.2), 9, 1.0, boxstyle="round,pad=0.2", 
        #                              linewidth=0, facecolor=item['color'], alpha=0.1, zorder=1)
        # ax.add_patch(rect)
        
        # Left accent bar
        rect_bar = patches.Rectangle((0.5, item['y'] - 1.0), 0.2, 0.8, color=item['color'])
        ax.add_patch(rect_bar)
        
        # Title
        ax.text(1.0, item['y'] - 0.4, item['title'], ha='left', va='center', fontsize=12, fontweight='bold', color=item['color'])
        
        # Stats
        ax.text(1.0, item['y'] - 0.7, item['stats'], ha='left', va='center', fontsize=11, fontweight='bold', color='#34495e')
        
        # Desc
        ax.text(1.0, item['y'] - 0.95, item['desc'], ha='left', va='center', fontsize=10, style='italic', color='#7f8c8d')
        
        # Checkmark
        ax.text(9.0, item['y'] - 0.6, "✓", ha='center', va='center', fontsize=20, color=item['color'])

    plt.tight_layout()
    plt.savefig('figures/Figure_7.3_Egypt_Opportunity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Figure_7.3_Egypt_Opportunity.png")

def create_privacy_calculus():
    """Generates the Privacy Calculus Framework Diagram"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, "PRIVACY CALCULUS FRAMEWORK", ha='center', va='center', fontsize=16, fontweight='bold', color='#2c3e50')
    ax.text(6, 7.0, "Rational Cost-Benefit Analysis", ha='center', va='center', fontsize=12, style='italic', color='#7f8c8d')
    
    # Left Box: Benefits
    box_benefits = patches.FancyBboxPatch((1, 4), 4, 2.5, boxstyle="round,pad=0.1", linewidth=2, edgecolor='#27ae60', facecolor='#eafaf1')
    ax.add_patch(box_benefits)
    ax.text(3, 6.2, "PERCEIVED BENEFITS", ha='center', va='center', fontweight='bold', color='#27ae60', fontsize=12)
    benefits_text = "• Premium discounts\n• Personalized wellness\n• Health feedback\n• Gamification rewards"
    ax.text(1.5, 5.2, benefits_text, ha='left', va='center', fontsize=11, color='#2c3e50')
    
    # Right Box: Risks
    box_risks = patches.FancyBboxPatch((7, 4), 4, 2.5, boxstyle="round,pad=0.1", linewidth=2, edgecolor='#c0392b', facecolor='#fdedec')
    ax.add_patch(box_risks)
    ax.text(9, 6.2, "PERCEIVED RISKS", ha='center', va='center', fontweight='bold', color='#c0392b', fontsize=12)
    risks_text = "• Data breach risk\n• Third-party sharing\n• Denial of coverage\n• Surveillance concerns"
    ax.text(7.5, 5.2, risks_text, ha='left', va='center', fontsize=11, color='#2c3e50')
    
    # Scale/Decision Logic (Center)
    ax.text(6, 3.5, "VS", ha='center', va='center', fontsize=14, fontweight='bold', color='#95a5a6')
    ax.arrow(3, 4, 1.5, -1.5, head_width=0.2, head_length=0.2, fc='#27ae60', ec='#27ae60')
    ax.arrow(9, 4, -1.5, -1.5, head_width=0.2, head_length=0.2, fc='#c0392b', ec='#c0392b')
    
    # Decision Box
    box_decision = patches.FancyBboxPatch((4, 1), 4, 1.5, boxstyle="round,pad=0.1", linewidth=2, edgecolor='#2980b9', facecolor='#ebf5fb')
    ax.add_patch(box_decision)
    ax.text(6, 2.0, "WILLINGNESS TO SHARE DATA", ha='center', va='center', fontweight='bold', color='#2980b9', fontsize=12)
    ax.text(6, 1.5, "(If Benefits > Risks)", ha='center', va='center', fontsize=11, style='italic', color='#2c3e50')
    
    # Footer: Moderators
    ax.text(6, 0.5, "Moderating Factors: Trust, Age, Health Status, Tech Literacy", ha='center', va='center', fontsize=10, style='italic', color='#7f8c8d')

    plt.tight_layout()
    plt.savefig('figures/Figure_4.3_Privacy_Calculus.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Figure_4.3_Privacy_Calculus.png")

if __name__ == "__main__":
    create_evolution_timeline()
    create_egypt_opportunity()
    create_privacy_calculus()
