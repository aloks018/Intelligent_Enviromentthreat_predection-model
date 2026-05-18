from __future__ import annotations

from typing import Dict, List


BUSINESS_PROFILES: Dict[str, Dict[str, object]] = {
    "Manufacturing": {
        "weights": {
            "air_risk": 0.28,
            "heat_risk": 0.16,
            "flood_risk": 0.18,
            "wind_risk": 0.08,
            "water_stress": 0.18,
            "climate_disruption": 0.12,
        },
        "focus": "plant uptime, workforce safety, and utility reliability",
    },
    "Logistics": {
        "weights": {
            "air_risk": 0.18,
            "heat_risk": 0.10,
            "flood_risk": 0.26,
            "wind_risk": 0.16,
            "water_stress": 0.08,
            "climate_disruption": 0.22,
        },
        "focus": "route continuity, delivery speed, and yard operations",
    },
    "Construction": {
        "weights": {
            "air_risk": 0.16,
            "heat_risk": 0.24,
            "flood_risk": 0.20,
            "wind_risk": 0.18,
            "water_stress": 0.08,
            "climate_disruption": 0.14,
        },
        "focus": "site safety, labor productivity, and material movement",
    },
    "Agriculture": {
        "weights": {
            "air_risk": 0.08,
            "heat_risk": 0.18,
            "flood_risk": 0.22,
            "wind_risk": 0.08,
            "water_stress": 0.28,
            "climate_disruption": 0.16,
        },
        "focus": "crop resilience, water availability, and field timing",
    },
    "Tourism": {
        "weights": {
            "air_risk": 0.24,
            "heat_risk": 0.18,
            "flood_risk": 0.16,
            "wind_risk": 0.08,
            "water_stress": 0.12,
            "climate_disruption": 0.22,
        },
        "focus": "visitor comfort, reputation, and service continuity",
    },
    "Office / IT Park": {
        "weights": {
            "air_risk": 0.22,
            "heat_risk": 0.14,
            "flood_risk": 0.18,
            "wind_risk": 0.06,
            "water_stress": 0.12,
            "climate_disruption": 0.28,
        },
        "focus": "employee wellbeing, commute reliability, and uptime planning",
    },
    "Real Estate": {
        "weights": {
            "air_risk": 0.12,
            "heat_risk": 0.12,
            "flood_risk": 0.26,
            "wind_risk": 0.08,
            "water_stress": 0.18,
            "climate_disruption": 0.24,
        },
        "focus": "asset value protection and long-term site attractiveness",
    },
}


EXPOSURE_MULTIPLIERS = {
    "Conservative": 1.12,
    "Balanced": 1.0,
    "Aggressive": 0.9,
}


def _clamp(value: float, lower: float = 0.0, upper: float = 100.0) -> float:
    return max(lower, min(upper, value))


def _scale(value: float, min_value: float, max_value: float) -> float:
    if max_value <= min_value:
        return 0.0
    return _clamp(((value - min_value) / (max_value - min_value)) * 100.0)


def _category(score: float) -> str:
    if score < 35:
        return "Low"
    if score < 55:
        return "Moderate"
    if score < 75:
        return "High"
    return "Severe"


def _continuity(score: float) -> str:
    if score < 35:
        return "Stable"
    if score < 55:
        return "Watch"
    if score < 75:
        return "At Risk"
    return "Critical"


def _recommendations(top_drivers: List[str], focus: str) -> List[str]:
    advice = {
        "air_risk": f"Protect {focus} by reducing outdoor exposure and checking ventilation readiness.",
        "heat_risk": f"Adjust shifts and cooling support to reduce heat pressure on {focus}.",
        "flood_risk": f"Review drainage, access roads, and backup routing to protect {focus}.",
        "wind_risk": f"Secure exposed equipment and inspect movement plans affecting {focus}.",
        "water_stress": f"Plan water storage, treatment, or alternate sourcing to support {focus}.",
        "climate_disruption": f"Build contingency buffers so sudden weather swings do not interrupt {focus}.",
    }
    return [advice[driver] for driver in top_drivers]


def calculate_business_impact(
    *,
    temperature: float,
    rainfall: float,
    humidity: float,
    wind_speed: float,
    aqi: float,
    business_type: str,
    exposure_level: str,
) -> Dict[str, object]:
    profile = BUSINESS_PROFILES.get(business_type, BUSINESS_PROFILES["Manufacturing"])
    weights = profile["weights"]
    focus = str(profile["focus"])

    air_risk = _scale(max(aqi, 0.0), 40.0, 260.0)
    heat_index_proxy = temperature + (humidity * 0.07)
    heat_risk = _scale(heat_index_proxy, 28.0, 52.0)
    flood_risk = _clamp((rainfall * 0.75) + (humidity * 0.25) - 12.0)
    wind_risk = _scale(wind_speed, 2.0, 22.0)
    water_stress = _clamp((temperature * 1.4) - (rainfall * 0.35) + ((100.0 - humidity) * 0.25))
    climate_disruption = _clamp((heat_risk * 0.28) + (flood_risk * 0.34) + (wind_risk * 0.18) + (air_risk * 0.20))

    components = {
        "air_risk": round(air_risk, 1),
        "heat_risk": round(heat_risk, 1),
        "flood_risk": round(flood_risk, 1),
        "wind_risk": round(wind_risk, 1),
        "water_stress": round(water_stress, 1),
        "climate_disruption": round(climate_disruption, 1),
    }

    weighted_score = 0.0
    for key, component_score in components.items():
        weighted_score += component_score * float(weights[key])

    score = _clamp(weighted_score * EXPOSURE_MULTIPLIERS.get(exposure_level, 1.0))
    category = _category(score)
    continuity = _continuity(score)
    sorted_drivers = sorted(components.items(), key=lambda item: item[1], reverse=True)
    top_drivers = [name for name, _ in sorted_drivers[:2]]

    driver_labels = {
        "air_risk": "Air pollution pressure",
        "heat_risk": "Heat stress",
        "flood_risk": "Rain and flood disruption",
        "wind_risk": "Wind disruption",
        "water_stress": "Water stress",
        "climate_disruption": "Climate volatility",
    }

    return {
        "score": round(score, 1),
        "category": category,
        "continuity": continuity,
        "components": {driver_labels[key]: value for key, value in components.items()},
        "top_driver": driver_labels[top_drivers[0]],
        "secondary_driver": driver_labels[top_drivers[1]],
        "recommendations": _recommendations(top_drivers, focus),
        "focus": focus,
    }
