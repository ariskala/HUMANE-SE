import numpy as np
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

humic_skills = np.array([
    "Analytical thinking",
    "Adaptability",
    "Artistic approach",
    "Assertiveness",
    "Assessment skills",
    "Brainstorming skills",
    "Bargaining skills",
    "Change management",
    "Colleagueship skills",
    "Conceptualization",
    "Community building skills",
    "Conflict management",
    "Conflict resolution",
    "Consistency",
    "Continuous learning",
    "Communication skills",
    "Coachability",
    "Collaboration skills",
    "Compassion",
    "Cooperation skills",
    "Courage to challenge",
    "Creativity",
    "Critical thinking",
    "Curiosity",
    "Decision-making skills",
    "Delegation",
    "Desire to learn",
    "Diligence",
    "Diplomatic skills",
    "Emotional support",
    "Empowerment",
    "Emotional intelligence",
    "Empathy",
    "Ethical thinking",
    "Facilitation skills",
    "Flexibility",
    "Focusing skills",
    "Goal-setting",
    "Growth Mindset",
    "Honesty",
    "Hybrid work skills",
    "Imagination",
    "Influencing skills",
    "Interaction skills",
    "Intercession skills",
    "Interview skills",
    "Integrity",
    "Interpersonal skills",
    "Judgment",
    "Justification",
    "Kindness",
    "Leadership skills",
    "Learning orientation",
    "Learning ability",
    "Listening skills",
    "Logical reasoning",
    "Management Skills",
    "Mentoring skills",
    "Mentalization",
    "Mindset",
    "Mind management",
    "Negotiation skills",
    "Observation skills",
    "Open-mindedness",
    "Organization skills",
    "Patience",
    "Persuasion",
    "Planning",
    "Power Skills",
    "Presentation skills",
    "Problem-solving",
    "Professionalism",
    "Public speaking",
    "Quick thinking",
    "Reflection",
    "Reliability",
    "Relationship building",
    "Resilience",
    "Resourcefulness",
    "Self-directed learning",
    "Self-knowledge",
    "Shared reflection",
    "Social skills",
    "Sparring skills",
    "Strategic thinking",
    "Stress management",
    "Supportiveness",
    "Team building",
    "Teamwork skills",
    "Thinking skills",
    "Trainability",
    "Trust-building",
    "Unbiased thinking",
    "User focus",
    "Valuing individuality",
    "Versatility",
    "Vision",
    "Visionary thinking",
    "Work-life balance",
    "Written communication"
])

file_path = "ESCO_Mapping_csv.csv"

esco_data = np.genfromtxt(
    file_path,
    delimiter=";",
    dtype=str,
    skip_header=1,
    usecols=(0,)
)

esco_skills = (
    esco_data[esco_data != ""]
    if esco_data.ndim > 0
    else np.array([])
)

humic_esco_list = []

for humic_skill in humic_skills:
    humic_embedding = model.encode(
        humic_skill,
        convert_to_tensor=True
    )

    for esco_skill in esco_skills:
        esco_embedding = model.encode(
            esco_skill,
            convert_to_tensor=True
        )

        similarity = util.pytorch_cos_sim(
            humic_embedding,
            esco_embedding
        ).item()

        if similarity > 0.5:
            humic_esco_list.append([
                humic_skill,
                esco_skill,
                similarity
            ])

humic_esco_array = np.array(
    humic_esco_list,
    dtype=object
)

np.savetxt(
    "humic_esco_matched_skills.csv",
    humic_esco_array,
    delimiter=";",
    fmt="%s",
    header="Humic Skill;ESCO Preferred Label;Similarity",
    comments=""
)

print(
    "Matching process completed. "
    "Results saved to humic_esco_matched_skills.csv."
)
