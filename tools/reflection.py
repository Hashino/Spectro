#!/usr/bin/env python3
"""
Spectro Learning Session Reflection Tool

A simple command-line tool to help educators and learners reflect on 
dupla-based learning sessions using Spectro methodology principles.
"""

import datetime
import json
import os
from pathlib import Path

class SpectroReflection:
    def __init__(self):
        self.session_data = {}
        self.reflection_dir = Path.home() / ".spectro_reflections"
        self.reflection_dir.mkdir(exist_ok=True)
    
    def gather_reflection(self):
        """Guide user through reflection process based on Spectro principles"""
        print("=== Spectro Learning Session Reflection ===\n")
        
        # Basic session info
        self.session_data['date'] = datetime.date.today().isoformat()
        self.session_data['participants'] = input("Who participated in this dupla? ")
        self.session_data['context'] = input("What was the learning context/subject? ")
        
        print("\n--- Core Principle Reflections ---")
        
        # Rule [/] - Never forget the question
        print("\n[/] Questions that drove today's learning:")
        questions = []
        while True:
            q = input("Enter a question (or press enter to continue): ")
            if not q:
                break
            questions.append(q)
        self.session_data['driving_questions'] = questions
        
        new_questions = []
        print("\nNew questions that emerged:")
        while True:
            q = input("Enter a new question (or press enter to continue): ")
            if not q:
                break
            new_questions.append(q)
        self.session_data['new_questions'] = new_questions
        
        # Rule [o] - Student controls learning
        self.session_data['learner_agency'] = input(
            "\n[o] How did the learner exercise agency/control today? "
        )
        
        # Rule [~] - Infinite love
        self.session_data['love_expressions'] = input(
            "\n[~] How was love/care expressed in this session? "
        )
        
        # Rule [=] - Self-care first  
        self.session_data['self_care'] = input(
            "\n[=] How did you practice self-care during this session? "
        )
        
        # General reflections
        print("\n--- General Reflection ---")
        self.session_data['went_well'] = input("What went well? ")
        self.session_data['challenges'] = input("What was challenging? ")
        self.session_data['insights'] = input("What insights emerged? ")
        self.session_data['next_steps'] = input("What are potential next steps? ")
        
    def save_reflection(self):
        """Save reflection to JSON file"""
        filename = f"reflection_{self.session_data['date']}.json"
        filepath = self.reflection_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.session_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Reflection saved to: {filepath}")
    
    def view_recent_reflections(self, days=7):
        """Display recent reflections"""
        print(f"\n=== Recent Reflections (last {days} days) ===")
        
        cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
        reflection_files = list(self.reflection_dir.glob("reflection_*.json"))
        
        recent_reflections = []
        for file in reflection_files:
            try:
                date_str = file.stem.split('_')[1]
                file_date = datetime.date.fromisoformat(date_str)
                if file_date >= cutoff_date:
                    recent_reflections.append((file_date, file))
            except (ValueError, IndexError):
                continue
        
        recent_reflections.sort(reverse=True)
        
        if not recent_reflections:
            print("No recent reflections found.")
            return
        
        for date, file in recent_reflections:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"\n--- {date} ---")
            print(f"Participants: {data.get('participants', 'N/A')}")
            print(f"Context: {data.get('context', 'N/A')}")
            print(f"Key Questions: {', '.join(data.get('driving_questions', []))}")
            if data.get('insights'):
                print(f"Insights: {data['insights']}")

def main():
    tool = SpectroReflection()
    
    print("Spectro Learning Reflection Tool")
    print("1. New reflection")
    print("2. View recent reflections") 
    print("3. Exit")
    
    choice = input("\nSelect an option: ")
    
    if choice == "1":
        tool.gather_reflection()
        tool.save_reflection()
        print("\n💝 Remember: The dupla never forgets the question.")
        
    elif choice == "2":
        days = input("How many days back to view? (default 7): ")
        try:
            days = int(days) if days else 7
        except ValueError:
            days = 7
        tool.view_recent_reflections(days)
        
    elif choice == "3":
        print("Keep questioning, keep loving. ❤️")
        
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()