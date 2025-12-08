
import io

refs = [
    "Abraham, M. (2016). Wearable technology: A health-and-care actuary's perspective. The Actuary.",
    "Banaee, H., Ahmed, M. U., & Loutfi, A. (2013). Data mining for wearable sensors in health monitoring systems: A review of recent trends and challenges. Sensors, 13(12), 17472-17500.",
    "CIPFA. (2015). Prevention: Better Than the Cure: Public Health and the Future of Healthcare Funding. CIPFA.org.",
    "Cisco. (2018). Cisco Edge-to-Enterprise IoT Analytics for Electric Utilities Solution Overview.",
    "Chen, Y., Qiu, W., Ou, R., & Huang, C. (2020). A contract-based insurance incentive mechanism boosted by wearable technology. IEEE Internet of Things Journal.",
    "Cox, D. R. (1972). Regression models and life-tables. Journal of the Royal Statistical Society: Series B (Methodological), 34(2), 187-202.",
    "de Zambotti, M., Rosas, L., Colrain, I. M., & Baker, F. C. (2017). The Sleep of the Ring: Comparison of the Oura Sleep Tracker Against Polysomnography. Behavioral Sleep Medicine, 1-15.",
    "Erdaş, Ç. B., & Güney, S. (2021). Human Activity Recognition by Using Different Deep Learning Approaches for Wearable Sensors.",
    "FinTech Global. (2019). Global InsurTech Funding Tops $3bn in 2018.",
    "Hafner, M., Pollard, J., & Van Stolk, C. (2018). Incentives and Physical Activity: An Assessment of the Association Between Vitality’s Active Rewards and Apple Watch Benefit. Rand Corporation.",
    "Horvath, S. (2013). DNA methylation age of human tissues and cell types. Genome Biology, 14(10), R115.",
    "Katzman, J. L., Shaham, U., Cloninger, A., Bates, J., Jiang, T., & Kluger, Y. (2018). DeepSurv: Personalized treatment recommender system using a Cox proportional hazards deep neural network. BMC Medical Research Methodology, 18(1), 24.",
    "Levine, M. E., Lu, A. T., Quach, A., Chen, B. H., Assimes, T. L., Bandinelli, S., ... & Horvath, S. (2018). An epigenetic biomarker of aging for lifespan and healthspan. Aging (Albany NY), 10(4), 573.",
    "Li, X., Dunn, J., Salins, D., et al. (2017). Digital Health: Tracking Physiomes and Activity Using Wearable Biosensors Reveals Useful Health-Related Information. PLoS Biology.",
    "Majumder, S., Mondal, T., & Deen, M. J. (2017). Wearable sensors for remote health monitoring. Sensors, 17(1), 130.",
    "McCrea, M., & Farrell, M. (2018). A conceptual model for pricing health and life insurance using wearable technology. Risk Management and Insurance Review, 21(3), 389-411.",
    "Missov, T., Németh, L., & Dańko, M. (2016). How much can we trust life tables? Sensitivity of mortality measures to right-censoring treatment. Palgrave Communications, 2, 15049.",
    "National Institute for Health and Care Excellence (NICE). (2014). Behavior Change: Individual Changes. Public Health Guideline.",
    "O'Neil, C. (2016). Weapons of math destruction: How big data increases inequality and threatens democracy. Crown.",
    "Schrack, J. A., Cooper, R., Al-Ghatrif, M., ... & NHANES Consortium. (2018). Calibrating the NHANES wrist-worn accelerometer to estimate physical activity in older adults. Journal of Gerontology: Series A, 73(10).",
    "Spender, A., Bullen, C., Altmann-Richer, L., et al. (2018). Wearables and the internet of things: considerations for the life and health insurance industry. British Actuarial Journal, 24, e22.",
    "Statista. (2018). Impact of health insurance on the use of connected health devices in Japan.",
    "Statista. (2019). Willingness to use insurance technologies for cheaper premium by technology U.S.",
    "Statista. (2021). Clinician's opinions on wearables use lowering health premiums by 2031.",
    "Vaupel, J. W., Manton, K. G., & Stallard, E. (1979). The impact of heterogeneity in individual frailty on the dynamics of mortality. Demography, 16(3), 439-454.",
    "Volpp, K. G., Asch, D. A., Galvin, R., & Loewenstein, G. (2011). Redesigning Employee Health Incentives—Lessons from Behavioral Economics. New England Journal of Medicine, 365, 388-390.",
    "Shim, J., Kim, H., Youn, J., et al. (2023). Wearable-based accelerometer activity profile as digital biomarker of inflammation, biological age, and mortality using hierarchical clustering analysis in NHANES 2011-2014. Nature Communications, 14, 7832. https://doi.org/10.1038/s41467-023-43681-6",
    "Pyrkov, T. V., Slipensky, K., Barg, M., et al. (2021). Extracting biological age from biomedical data via deep learning: Too much of a good thing? Scientific Reports, 11, 5210. https://doi.org/10.1038/s41598-021-84345-3",
    "Egyptian Financial Regulatory Authority (FRA). (2023). Insurance Market Report 2023. FRA Publications, Cairo, Egypt.",
    "Accenture. (2019). Global Financial Services Consumer Study: Insurance. Accenture Research, pp. 1-24. https://www.accenture.com/us-en/insights/financial-services/global-financial-services-consumer-study",
    "Park, S., Choi, J., Lee, S., et al. (2021). Determinants of consumers' adoption of wearable-based health insurance. JMIR mHealth and uHealth, 9(9), e14074. https://doi.org/10.2196/14074",
    "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions (SHAP). Advances in Neural Information Processing Systems, 30.",
    "Nienaber, A. M., Hofeditz, M., & Searle, R. (2023). Trust and willingness to share personal health data with insurers. Journal of Risk and Insurance, 90(2), 389-418.",
    "GlobalData. (2022). Consumer Insurance Survey: Attitudes Towards Wearable Technology in Insurance. GlobalData Financial Services, London.",
    "LIMRA/LOMA. (2024). 2024 Insurance Barometer Study: Consumer Attitudes on Wellness Programs. LIMRA Research, Hartford, CT.",
    "Gen Re. (2021). Wearables and Health Insurance: A German Consumer Study. Gen Reinsurance Research, Cologne.",
    "ValuePenguin. (2022). Fitness Trackers and Health Insurance Discounts Survey. LendingTree Research, Charlotte, NC.",
    "Culnan, M. J., & Armstrong, P. K. (1999). Information privacy concerns, procedural fairness, and impersonal trust. Organization Science, 10(1), 104-115.",
    "Dinev, T., & Hart, P. (2006). An extended privacy calculus model for e-commerce transactions. Information Systems Research, 17(1), 61-80.",
    "Xu, H., Luo, X., Carroll, J. M., & Rosson, M. B. (2011). The personalization privacy paradox. Information Technology & People, 24(4), 315-334.",
    "Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving decisions about health, wealth, and happiness. Yale University Press.",
    "Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.",
    "Vitality Group & London School of Economics. (2023). Seven-Year Impact Study: Wearables and Mortality Outcomes. LSE Health Working Paper.",
    "AIA Vitality Australia. (2021). Member Engagement and Retention Report. AIA Group Research, Sydney.",
    "McKinsey & Company. (2023). The future of insurance: How artificial intelligence is transforming the industry. McKinsey Global Institute.",
    "Swiss Re. (2024). Global Insurance Market Outlook 2024. Swiss Re Institute, Zurich.",
    "Deloitte. (2024). Insurance outlook 2024: Navigating transformation through technology and innovation. Deloitte Center for Financial Services.",
    "Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.",
    "Henckaerts, R., Côte, M. P., Antonio, K., & Verbelen, R. (2018). Boosting insights in insurance tariff plans with tree-based machine learning methods. North American Actuarial Journal, 22(2), 255-285.",
    "Richman, R. (2021). Machine learning with applications in actuarial science. North American Actuarial Journal, 25(sup1), S315-S321.",
    "Wüthrich, M. V., & Merz, M. (2023). Statistical foundations of actuarial learning and its applications. Springer Actuarial.",
    "GSMA. (2024). Mobile Economy Middle East and North Africa 2024. GSMA Intelligence, London.",
    "International Diabetes Federation (IDF). (2023). IDF Diabetes Atlas 10th Edition. IDF Publications, Brussels.",
    "Brooks, B., Hershfield, H. E., & Shu, S. B. (2020). The future self in insurance and retirement savings decisions. Journal of Risk and Insurance, 87(4), 917-943.",
    "John Hancock. (2018). John Hancock Adds Interactive Element to All New Life Insurance Policies. Press Release, Boston, MA.",
    "NAIC. (2023). Model Bulletin on the Use of Artificial Intelligence in Insurance. NAIC Publications.",
    "EIOPA. (2024). Guidelines on the Use of Artificial Intelligence in Insurance. EIOPA Publications.",
    "European Union. (2018). General Data Protection Regulation (GDPR). Regulation (EU) 2016/679.",
    "Discovery Health. (2020). Vitality Digital Innovation Report. Discovery Limited, Johannesburg.",
    "Generali. (2023). Annual Report: Vitality Program Performance. Generali Group, Trieste."
]

def clean_ref(ref):
    return ref.strip().strip("',")

cleaned_refs = [clean_ref(r) for r in refs]
sorted_refs = sorted(cleaned_refs, key=lambda x: x.lower())

# Writing Markdown file
with open('sorted_references.md', 'w', encoding='utf-8') as f:
    for i, ref in enumerate(sorted_refs, 1):
        try:
            parts = ref.split(". ", 1)
            author = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            f.write(f"{i}. **{author}.** {rest}\n")
        except:
            f.write(f"{i}. {ref}\n")

# Writing LaTeX file
with open('sorted_references.tex', 'w', encoding='utf-8') as f:
    f.write("\\begin{enumerate}\n")
    for ref in sorted_refs:
        # LaTeX escaping special chars if necessary - minimal escaping here
        ref_tex = ref.replace("&", "\&").replace("%", "\%")
        # Italicizing journal names is hard without structure, so we leave as text or try heuristic
        # Heuristic: try to italicize text after last period? No, too risky.
        # Just writing cleanly.
        f.write(f"\\item {ref_tex}\n")
    f.write("\\end{enumerate}\n")
