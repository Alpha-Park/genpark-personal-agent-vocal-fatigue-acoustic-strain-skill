# -*- coding: utf-8 -*-
"""
Personal Agent Vocal Fatigue Acoustic Strain Client
Zero-dependency Titze vocal dose collision stress modeler, cumulative speaking
strain auditor, and vocal cord restoration rest protocol prescriber.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentVocalFatigueAcousticStrain:
    """
    Protects voice stamina for remote workers, speakers, and executives.
    Calculates vocal fold collision doses, models acoustic strain, and prescribes rest protocols.
    """

    def calculate_vocal_collision_dose_and_stress(
        self,
        speaking_duration_minutes: float,
        average_spl_db: float = 68.0,
        fundamental_freq_f0_hz: float = 130.0
    ) -> Dict[str, Any]:
        """
        Titze Vocal Dose Model:
        Cycle Dose D_cycle = f0 * (speaking_minutes * 60 * 0.70 voicing duty factor).
        Impact Stress = SPL * (f0 / 100)^0.7 * (Minutes / 60).
        """
        dur_min = max(1.0, float(speaking_duration_minutes))
        spl = max(40.0, min(100.0, float(average_spl_db)))
        f0 = max(80.0, min(350.0, float(fundamental_freq_f0_hz)))

        # 70% voicing duty cycle during active speech
        voiced_seconds = dur_min * 60.0 * 0.70
        total_vocal_fold_collisions = int(f0 * voiced_seconds)

        # Impact stress accumulation
        impact_stress_units = round(spl * math.pow(f0 / 100.0, 0.7) * (dur_min / 60.0), 1)

        if impact_stress_units >= 250.0:
            tier = "SEVERE_VOCAL_STRAIN_HIGH_RISK"
        elif impact_stress_units >= 120.0:
            tier = "MODERATE_VOCAL_FATIGUE"
        elif impact_stress_units >= 50.0:
            tier = "LIGHT_VOCAL_LOAD"
        else:
            tier = "NEGLIGIBLE_STRAIN"

        return {
            "speaking_duration_minutes": dur_min,
            "sound_pressure_level_db": spl,
            "fundamental_frequency_hz": f0,
            "vocal_fold_collision_count": total_vocal_fold_collisions,
            "cumulative_impact_stress_score": impact_stress_units,
            "vocal_strain_tier": tier,
            "phonation_overload_status": impact_stress_units >= 180.0
        }

    def evaluate_dysphonia_and_vocal_fatigue_risk(
        self,
        cumulative_speaking_hours_today: float,
        hydration_status_score: float = 0.80
    ) -> Dict[str, Any]:
        """
        Evaluates risk of vocal hoarseness and mucosal fatigue.
        Risk Score = min(100, (SpeakingHours / 5.0) * 80 * (1.5 - Hydration)).
        """
        hours = max(0.0, float(cumulative_speaking_hours_today))
        hydration = max(0.1, min(1.0, float(hydration_status_score)))

        # Poor hydration thickens vocal fold mucus, multiplying collision shear stress
        hydration_penalty = 1.5 - (hydration * 0.5)
        raw_risk = (hours / 4.5) * 65.0 * hydration_penalty
        risk_score = round(max(0.0, min(100.0, raw_risk)), 1)

        if risk_score >= 70.0:
            diagnosis = "IMMINENT_VOCAL_FATIGUE_DYSPHONIA"
            advice = "Enforce immediate silent vocal rest; hydrate with warm water/steam inhalation."
        elif risk_score >= 40.0:
            diagnosis = "ELEVATED_LARYNGEAL_TENSION"
            advice = "Adopt conversational softer volume (<65 dB); perform gentle lip trills."
        else:
            diagnosis = "ROBUST_VOCAL_HEALTH"
            advice = "Maintain current speaking pace."

        return {
            "cumulative_speaking_hours": hours,
            "hydration_status_score": hydration,
            "vocal_fatigue_risk_score": risk_score,
            "diagnosis": diagnosis,
            "clinical_guidance": advice,
            "recommended_maximum_remaining_speaking_hours": round(max(0.0, 5.0 - hours), 1)
        }

    def prescribe_vocal_recovery_and_rest_protocol(
        self,
        current_fatigue_score: float,
        upcoming_speech_minutes: float = 45.0
    ) -> Dict[str, Any]:
        """
        Prescribes timed vocal rest, semi-occluded vocal tract (SOVT) exercises, and hydration pauses.
        """
        score = max(0.0, min(100.0, float(current_fatigue_score)))
        speech_min = max(0.0, float(upcoming_speech_minutes))

        # Rest minutes required
        rest_minutes = max(5, int(score * 0.35))

        exercises = []
        if score >= 50.0:
            exercises.append("Straw phonation: 3 minutes of gentle pitch glides into a glass of water")
            exercises.append("Complete silent vocal rest for 15 minutes before next meeting")
        else:
            exercises.append("Lip trills: 2 minutes of relaxed ascending and descending glides")
            exercises.append("Hydration pause: 250ml room temperature water")

        return {
            "current_vocal_fatigue_score": score,
            "mandatory_silent_rest_minutes": rest_minutes,
            "sovt_rehabilitation_exercises": exercises,
            "upcoming_speech_duration_minutes": speech_min,
            "volume_cap_recommendation_db": 62.0 if score >= 60.0 else 70.0
        }
