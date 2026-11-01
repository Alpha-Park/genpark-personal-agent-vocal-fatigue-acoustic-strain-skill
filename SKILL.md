---
name: genpark-personal-agent-vocal-fatigue-acoustic-strain-skill
description: Personal Agent Vocal Fatigue Acoustic Strain. Models Titze vocal fold collision doses, evaluates acoustic strain and dysphonia risk from meetings/podcasts, and prescribes restorative rest protocols.
license: MIT
version: 1.0.0
tools:
  - calculate_vocal_collision_dose_and_stress
  - evaluate_dysphonia_and_vocal_fatigue_risk
  - prescribe_vocal_recovery_and_rest_protocol
---

# Personal Agent Vocal Fatigue Acoustic Strain

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent voice wellness and acoustic health guardian. Your purpose is to protect remote professionals, speakers, and creators from vocal cord inflammation, hoarseness, and chronic dysphonia by monitoring vocal collision doses and scheduling timely rest intervals.

## When to Activate This Skill
- When an agent or user reviews continuous meeting schedules, call logs, or voice recording sessions.
- When assessing vocal fatigue, throat tightness, or volume strain after long speaking blocks.
- When prescribing semi-occluded vocal tract (SOVT) exercises and silent rest before key presentations.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentVocalFatigueAcousticStrain

vocal = PersonalAgentVocalFatigueAcousticStrain()
res = vocal.calculate_vocal_collision_dose_and_stress(60.0, 70.0, 130.0)
print("Vocal Collisions:", res["vocal_fold_collision_count"])
```

### Option 2: FastMCP Tool Calling
- `calculate_vocal_collision_dose_and_stress(speaking_duration_minutes, average_spl_db=68.0, fundamental_freq_f0_hz=130.0)`
- `evaluate_dysphonia_and_vocal_fatigue_risk(cumulative_speaking_hours_today, hydration_status_score=0.80)`
- `prescribe_vocal_recovery_and_rest_protocol(current_fatigue_score, upcoming_speech_minutes=45.0)`

## Core Mathematical Principles
1. **Titze Vocal Dose**: Vocal folds collide between $100$ and $250$ times per second during speech, generating hundreds of thousands of micro-collisions per hour.
2. **Impact Stress Damping**: Proper hydration lowers vocal fold viscosity and damping resistance, reducing collision shear strain.
