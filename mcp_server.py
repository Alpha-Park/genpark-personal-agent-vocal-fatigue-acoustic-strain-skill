# -*- coding: utf-8 -*-
"""
Personal Agent Vocal Fatigue Acoustic Strain FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentVocalFatigueAcousticStrain

mcp = FastMCP("genpark-personal-agent-vocal-fatigue-acoustic-strain-skill")
vocal = PersonalAgentVocalFatigueAcousticStrain()

@mcp.tool()
def calculate_vocal_collision_dose_and_stress(
    speaking_duration_minutes: float,
    average_spl_db: float = 68.0,
    fundamental_freq_f0_hz: float = 130.0
) -> str:
    """
    Calculates vocal fold collision count and acoustic impact stress from speaking sessions.
    """
    res = vocal.calculate_vocal_collision_dose_and_stress(speaking_duration_minutes, average_spl_db, fundamental_freq_f0_hz)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_dysphonia_and_vocal_fatigue_risk(
    cumulative_speaking_hours_today: float,
    hydration_status_score: float = 0.80
) -> str:
    """
    Evaluates vocal fatigue risk and hoarseness probability based on speaking hours and hydration.
    """
    res = vocal.evaluate_dysphonia_and_vocal_fatigue_risk(cumulative_speaking_hours_today, hydration_status_score)
    return json.dumps(res, indent=2)

@mcp.tool()
def prescribe_vocal_recovery_and_rest_protocol(
    current_fatigue_score: float,
    upcoming_speech_minutes: float = 45.0
) -> str:
    """
    Prescribes targeted vocal rest intervals and SOVT rehabilitation exercises.
    """
    res = vocal.prescribe_vocal_recovery_and_rest_protocol(current_fatigue_score, upcoming_speech_minutes)
    return json.dumps(res, indent=2)

def main():
    print("Testing Vocal Fatigue Acoustic Strain FastMCP Server:")
    print(calculate_vocal_collision_dose_and_stress(60.0, 72.0, 135.0))

if __name__ == "__main__":
    main()
