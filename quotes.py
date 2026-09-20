import random

# ---------------------------------------------------------
# Trading Quotes (30% chance)
# ---------------------------------------------------------
TRADING_QUOTES = [
    "“In trading, your job is not to predict, but to manage risk.”",
    "“The market transfers money from the impatient to the patient.”",
    "“Losses are tuition. Keep the school cheap.”",
    "“Survive first. Thrive later.”",
    "“Small edges, applied consistently, become big outcomes.”",
    "“Your edge is useless if your emotions override your rules.”",
    "“Flat is a position. Doing nothing is a decision.”",
    "“Protect your mind; it's your real trading capital.”",
]

# ---------------------------------------------------------
# Clone Wars Quotes (70% chance)
# Format: "Season X, Episode Y: “Quote”"
# ---------------------------------------------------------
CLONE_WARS_QUOTES = [

    # -------------------------
    # SEASON 1
    # -------------------------
    "Season 1, Episode 1: “Great leaders inspire greatness in others.”",
    "Season 1, Episode 2: “Belief is not a matter of choice, but of conviction.”",
    "Season 1, Episode 3: “Easy is the path to wisdom for those not blinded by ego.”",
    "Season 1, Episode 4: “A plan is only as good as those who see it through.”",
    "Season 1, Episode 5: “The best confidence builder is experience.”",
    "Season 1, Episode 6: “Trust in your friends, and they'll have reason to trust in you.”",
    "Season 1, Episode 7: “You hold onto friends by keeping your heart a little softer than your head.”",
    "Season 1, Episode 8: “Heroes are made by the times.”",
    "Season 1, Episode 9: “Ignore your instincts at your peril.”",
    "Season 1, Episode 10: “Most powerful is he who controls his own power.”",
    "Season 1, Episode 11: “The winding path to peace is always a worthy one, regardless of how many turns it takes.”",
    "Season 1, Episode 12: “Fail with honor rather than succeed by fraud.”",
    "Season 1, Episode 13: “Greed and fear of loss are the roots that lead to the tree of evil.”",
    "Season 1, Episode 14: “When surrounded by war, one must eventually choose a side.”",
    "Season 1, Episode 15: “Arrogance diminishes wisdom.”",
    "Season 1, Episode 16: “Truth enlightens the mind, but won't always bring happiness to your heart.”",
    "Season 1, Episode 17: “Fear is a disease; hope is its only cure.”",
    "Season 1, Episode 18: “A single chance is a galaxy of hope.”",
    "Season 1, Episode 19: “It is a rough road that leads to the heights of greatness.”",
    "Season 1, Episode 20: “The costs of war can never be truly accounted for.”",
    "Season 1, Episode 21: “Compromise is a virtue to be cultivated, not a weakness to be despised.”",
    "Season 1, Episode 22: “A secret shared is a trust formed.”",

    # -------------------------
    # SEASON 2
    # -------------------------
    "Season 2, Episode 1: “A lesson learned is a lesson earned.”",
    "Season 2, Episode 2: “Overconfidence is the most dangerous form of carelessness.”",
    "Season 2, Episode 3: “The first step to correcting a mistake is patience.”",
    "Season 2, Episode 4: “A true heart should never be doubted.”",
    "Season 2, Episode 5: “Believe in yourself or no one else will.”",
    "Season 2, Episode 6: “No gift is more precious than trust.”",
    "Season 2, Episode 7: “Sometimes, accepting help is harder than offering it.”",
    "Season 2, Episode 8: “Attachment is not compassion.”",
    "Season 2, Episode 9: “For everything you gain, you lose something else.”",
    "Season 2, Episode 10: “It is the quest for honor that makes one honorable.”",
    "Season 2, Episode 11: “Easy isn't always simple.”",
    "Season 2, Episode 12: “If you ignore the past, you jeopardize the future.”",
    "Season 2, Episode 13: “Fear not for the future, weep not for the past.”",
    "Season 2, Episode 14: “In war, truth is the first casualty.”",
    "Season 2, Episode 15: “Searching for the truth is easy. Accepting the truth is hard.”",
    "Season 2, Episode 16: “A wise leader knows when to follow.”",
    "Season 2, Episode 17: “Courage makes heroes, but trust builds friendships.”",
    "Season 2, Episode 18: “Choose what is right, not what is easy.”",
    "Season 2, Episode 19: “The most dangerous beast is the beast within.”",
    "Season 2, Episode 20: “Who my father was matters less than my memory of him.”",
    "Season 2, Episode 21: “Adversity is a friendship's truest test.”",
    "Season 2, Episode 22: “Revenge is a confession of pain.”",

    # -------------------------
    # SEASON 3
    # -------------------------
    "Season 3, Episode 1: “Brothers in arms are brothers for life.”",
    "Season 3, Episode 2: “Fighting a war tests a soldier's skills, defending his home tests a soldier's heart.”",
    "Season 3, Episode 3: “Where there's a will, there's a way.”",
    "Season 3, Episode 4: “A child stolen is a hope lost.”",
    "Season 3, Episode 5: “The challenge of hope is to overcome corruption.”",
    "Season 3, Episode 6: “Those who enforce the law must obey the law.”",
    "Season 3, Episode 7: “The future has many paths, choose wisely.”",
    "Season 3, Episode 8: “A failure in planning is a plan for failure.”",
    "Season 3, Episode 9: “Love comes in all shapes and sizes.”",
    "Season 3, Episode 10: “Fear is a great motivator.”",
    "Season 3, Episode 11: “Truth can strike down the spectre of fear.”",
    "Season 3, Episode 12: “The swiftest path to destruction is through vengeance.”",
    "Season 3, Episode 13: “Evil is not born, it is taught.”",
    "Season 3, Episode 14: “The path to evil may bring great power, but not loyalty.”",
    "Season 3, Episode 15: “Balance is found in the one who faces his guilt.”",
    "Season 3, Episode 16: “He who surrenders hope, surrenders life.”",
    "Season 3, Episode 17: “He who seeks to control fate shall never find peace.”",
    "Season 3, Episode 18: “Adaptation is the key to survival.”",
    "Season 3, Episode 19: “Anything that can go wrong will.”",
    "Season 3, Episode 20: “Without honor, victory is hollow.”",
    "Season 3, Episode 21: “Without humility, courage is a dangerous game.”",
    "Season 3, Episode 22: “A great student is what the teacher hopes to be.”",

    # -------------------------
    # SEASON 4
    # -------------------------
    "Season 4, Episode 1: “When destiny calls, the chosen have no choice.”",
    "Season 4, Episode 2: “Only through fire is a strong sword forged.”",
    "Season 4, Episode 3: “Crowns are inherited, kingdoms are earned.”",
    "Season 4, Episode 4: “Who a person truly is cannot be seen with the eye.”",
    "Season 4, Episode 5: “Understanding is honoring the truth beneath the surface.”",
    "Season 4, Episode 6: “Who's the more foolish, the fool or the fool who follows him?”",
    "Season 4, Episode 7: “The first step towards loyalty is trust.”",
    "Season 4, Episode 8: “The path of ignorance is guided by fear.”",
    "Season 4, Episode 9: “The wise man leads, the strong man follows.”",
    "Season 4, Episode 10: “Our actions define our legacy.”",
    "Season 4, Episode 11: “Where we are going always reflects where we came from.”",
    "Season 4, Episode 12: “Those who enslave others, inevitably become slaves themselves.”",
    "Season 4, Episode 13: “Great hope can come from small sacrifices.”",
    "Season 4, Episode 14: “Friendship shows us who we really are.”",
    "Season 4, Episode 15: “All warfare is based on deception.”",
    "Season 4, Episode 16: “Keep your friends close, but keep your enemies closer.”",
    "Season 4, Episode 17: “The strong survive, the noble overcome.”",
    "Season 4, Episode 18: “Trust is the greatest of gifts, but it must be earned.”",
    "Season 4, Episode 19: “One must let go of the past to hold on to the future.”",
    "Season 4, Episode 20: “Who we are never changes, who we think we are does.”",
    "Season 4, Episode 21: “A fallen enemy may rise again, but the reconciled one is truly vanquished.”",
    "Season 4, Episode 22: “The enemy of my enemy is my friend.”",

    # -------------------------
    # SEASON 5
    # -------------------------
    "Season 5, Episode 1: “Strength of character can defeat strength in numbers.”",
    "Season 5, Episode 2: “Fear is a malleable weapon.”",
    "Season 5, Episode 3: “To seek something is to believe in its possibility.”",
    "Season 5, Episode 4: “Struggles often begin and end with the truth.”",
    "Season 5, Episode 5: “Disobedience is a demand for change.”",
    "Season 5, Episode 6: “He who faces himself, finds himself.”",
    "Season 5, Episode 7: “The young are often underestimated.”",
    "Season 5, Episode 8: “When we rescue others, we rescue ourselves.”",
    "Season 5, Episode 9: “Choose your enemies wisely, as they may be your last hope.”",
    "Season 5, Episode 10: “Humility is the only defense against humiliation.”",
    "Season 5, Episode 11: “When all seems hopeless, a true hero gives hope.”",
    "Season 5, Episode 12: “A soldier's most powerful weapon is courage.”",
    "Season 5, Episode 13: “You must trust in others or success is impossible.”",
    "Season 5, Episode 14: “One vision can have many interpretations.”",
    "Season 5, Episode 15: “Alliances can stall true intentions.”",
    "Season 5, Episode 16: “Morality separates heroes from villains.”",
    "Season 5, Episode 17: “Sometimes even the smallest doubt can shake the greatest belief.”",
    "Season 5, Episode 18: “Courage begins by trusting oneself.”",
    "Season 5, Episode 19: “Never become desperate enough to trust the untrustworthy.”",
    "Season 5, Episode 20: “Never give up hope, no matter how dark things seem.”",

    # -------------------------
    # SEASON 6
    # -------------------------
    "Season 6, Episode 1: “The truth about yourself is always the hardest to accept.”",
    "Season 6, Episode 2: “The wise benefit from a second opinion.”",
    "Season 6, Episode 3: “When in doubt, go to the source.”",
    "Season 6, Episode 4: “The popular belief isn't always the correct one.”",
    "Season 6, Episode 5: “To love, is to trust. To trust is to believe.”",
    "Season 6, Episode 6: “Jealousy is the path to chaos.”",
    "Season 6, Episode 7: “Deceit is the weapon of greed.”",
    "Season 6, Episode 8: “Without darkness there cannot be light.”",
    "Season 6, Episode 9: “Wisdom is born in fools as well as wise men.”",
    "Season 6, Episode 10: “What is lost is often found.”",
    "Season 6, Episode 11: “Madness can sometimes be the path to truth.”",
    "Season 6, Episode 12: “Death is just the beginning.”",
    "Season 6, Episode 13: “Facing all that you fear will free you from yourself.”",

    # -------------------------
    # SEASON 7
    # -------------------------
    "Season 7, Episode 1: “Embrace others for their differences, for that makes you whole.”",
    "Season 7, Episode 2: “The search for truth begins with belief.”",
    "Season 7, Episode 3: “Survival is one step on the path to living.”",
    "Season 7, Episode 4: “Trust placed in another is trust earned.”",
    "Season 7, Episode 5: “If there is no path before you, create your own.”",
    "Season 7, Episode 6: “Mistakes are valuable lessons often learned too late.”",
    "Season 7, Episode 7: “Who you were does not have to define who you are.”",
    "Season 7, Episode 8: “You can change who you are, but you cannot run from yourself.”",
]

# ---------------------------------------------------------
# Weighted Random Quote Generator
# ---------------------------------------------------------
def get_random_quote():
    """Return a random quote with 70% Clone Wars / 30% trading weighting."""
    if random.random() < 0.7:
        quote = random.choice(CLONE_WARS_QUOTES)
    else:
        quote = random.choice(TRADING_QUOTES)
    return f"*{quote}*"
