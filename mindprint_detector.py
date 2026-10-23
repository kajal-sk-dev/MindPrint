"""
MindPrint Detector - Core AI Detection Engine
Detects human vs AI code/writing patterns
"""

import re
import math
from collections import Counter

class MindPrintDetector:
    def __init__(self):
        self.ai_patterns = [
            r'As an AI language model',
            r'In conclusion,',
            r'Furthermore,',
            r'Moreover,',
            r'It is important to note that',
            r'"""[\s\S]*?Args:[\s\S]*?Returns:[\s\S]*?"""',  # Over-documented docstring
            r'from typing import',
            r'List\[int\] -> List\[int\]',
            r'def main\(\):',
            r'if __name__ == "__main__":\s*main\(\)'
        ]
        
        self.human_patterns = [
            r'# .*lol',
            r'# .*hope it works',
            r'# .*mess',
            r'# quick.*before submission',
            r'temp = ',
            r'# i always',
            r'print\(.*\) #',
        ]

    def calculate_entropy(self, text):
        """Higher entropy = more human-like"""
        if not text:
            return 0
        freq = Counter(text)
        length = len(text)
        entropy = -sum((count/length) * math.log2(count/length) for count in freq.values())
        return entropy

    def analyze(self, code_text):
        """Main analysis function"""
        code_text_lower = code_text.lower()
        
        ai_score = 0
        human_score = 0
        reasons = []

        # Check AI patterns
        for pattern in self.ai_patterns:
            if re.search(pattern, code_text, re.IGNORECASE):
                ai_score += 15
                reasons.append(f"AI Pattern detected: {pattern[:30]}")

        # Check Human patterns
        for pattern in self.human_patterns:
            if re.search(pattern, code_text, re.IGNORECASE):
                human_score += 20
                reasons.append(f"Human Pattern: messy/real comment")

        # Entropy check
        entropy = self.calculate_entropy(code_text)
        if entropy > 4.5:
            human_score += 10
            reasons.append(f"High entropy {entropy:.2f} = human-like variance")
        else:
            ai_score += 10
            reasons.append(f"Low entropy {entropy:.2f} = AI-like consistency")

        # Comment ratio
        comment_lines = len(re.findall(r'#.*', code_text))
        total_lines = len(code_text.split('\n'))
        comment_ratio = comment_lines / max(total_lines, 1)
        
        if comment_ratio > 0.3 and "Args:" in code_text:
            ai_score += 15
            reasons.append("Over-documented = AI style")

        # Final calculation
        total = ai_score + human_score
        if total == 0:
            ai_percent = 50
        else:
            ai_percent = (ai_score / total) * 100

        human_percent = 100 - ai_percent

        if ai_percent > 60:
            verdict = "AI Generated"
        elif human_percent > 60:
            verdict = "Human Written"
        else:
            verdict = "Mixed / Uncertain"

        return {
            "ai_score": round(ai_percent, 2),
            "human_score": round(human_percent, 2),
            "verdict": verdict,
            "entropy": round(entropy, 2),
            "reasons": reasons[:5]
        }

# For testing
if __name__ == "__main__":
    detector = MindPrintDetector()
    sample = open("samples/human_code.py").read()
    print(detector.analyze(sample))
