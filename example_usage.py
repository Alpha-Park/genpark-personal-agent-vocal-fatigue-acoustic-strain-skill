# -*- coding: utf-8 -*-
import json
from client import PersonalAgentVocalFatigueAcousticStrain

vocal = PersonalAgentVocalFatigueAcousticStrain()

print("=" * 64)
print("DEMO: Personal Vocal Fatigue & Acoustic Strain Auditor")
print("=" * 64)

# 1. Calculate vocal collision dose
dose = vocal.calculate_vocal_collision_dose_and_stress(speaking_duration_minutes=90.0, average_spl_db=72.0, fundamental_freq_f0_hz=140.0)
print(f"\n1. Vocal Collision Dose (90-min Call at 72 dB):")
print(f"   Vocal Fold Collisions: {dose['vocal_fold_collision_count']:,} collisions")
print(f"   Cumulative Impact Stress: {dose['cumulative_impact_stress_score']} ({dose['vocal_strain_tier']})")

# 2. Evaluate dysphonia risk
risk = vocal.evaluate_dysphonia_and_vocal_fatigue_risk(cumulative_speaking_hours_today=4.5, hydration_status_score=0.60)
print(f"\n2. Daily Dysphonia Risk (4.5h Speech | 60% Hydration):")
print(f"   Fatigue Risk Score: {risk['vocal_fatigue_risk_score']}/100 ({risk['diagnosis']})")
print(f"   Clinical Guidance: {risk['clinical_guidance']}")

# 3. Prescribe vocal recovery protocol
rx = vocal.prescribe_vocal_recovery_and_rest_protocol(current_fatigue_score=risk['vocal_fatigue_risk_score'], upcoming_speech_minutes=30.0)
print(f"\n3. Vocal Rest & Rehabilitation Prescription:")
print(f"   Mandatory Silent Rest: {rx['mandatory_silent_rest_minutes']} minutes")
print(f"   Volume Cap Recommendation: {rx['volume_cap_recommendation_db']} dB")
for ex in rx['sovt_rehabilitation_exercises']:
    print(f"   -> {ex}")
