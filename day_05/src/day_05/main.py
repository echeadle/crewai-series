#!/usr/bin/env python
import sys
from crew import Day05Crew
from dotenv import load_dotenv

load_dotenv()

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'is tesla in trouble',
    
    }
    Day05Crew().crew().kickoff(inputs=inputs)

run()
