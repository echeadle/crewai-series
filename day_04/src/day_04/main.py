#!/usr/bin/env python
import sys
from crew import Day03Crew
from datetime import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        # 'topic': 'Judge Ryan D. Tenny, judge Court of appeals',
        'topic': 'Arnold Palmer',
    
    }
    Day03Crew().crew().kickoff(inputs=inputs)

run()
