def formulate_description(pays, year, predictions):
    description = f"En {year} pour {pays}, "

    # Espérance de vie
    life = predictions["life"]
    if life >= 64:
        description += f"l'espérance de vie sera remarquablement haute à {life} ans, "
    elif life <= 55:
        description += f"l'espérance de vie sera relativement basse à {life} ans, "
    else:
        description += f"l'espérance de vie sera de {life} ans, "

    # Mortalité adulte
    adult_mortality = predictions["adultMortality"]
    if adult_mortality > 100:
        description += "indiquant une mortalité adulte élevée, "
    else:
        description += "avec une mortalité adulte modérée, "

    # Mortalité infantile
    infant_mortality = predictions["infantMortality"]
    if infant_mortality > 50:
        description += "accompagnée d'une forte mortalité infantile, "
    else:
        description += "et une mortalité infantile relativement faible, "

    # Éducation
    schooling = predictions["schooling"]
    description += f"et une durée moyenne d'éducation de {schooling} années. "

    # Décès des moins de cinq ans
    under_five_death = predictions["underFiveDeath"]
    if under_five_death > 1000:
        description += f"Un nombre élevé de décès chez les moins de cinq ans est prévu, avec {under_five_death} cas, "
    else:
        description += (
            f"avec {under_five_death} décès attendus chez les moins de cinq ans, "
        )

    # Croissance de la population
    population_growth = predictions["population"]
    if population_growth < 0:
        description += "marquant une diminution inquiétante de la population. "
    elif population_growth > 2:
        description += "signifiant une croissance rapide de la population. "
    else:
        description += "indiquant une croissance démographique stable. "

    # Consommation d'alcool
    alcohol = predictions["alcohol"]
    if alcohol > 9:
        description += f"La consommation d'alcool sera exceptionnellement élevée à {alcohol} litres par habitant."
    elif alcohol < 5:
        description += f"La consommation d'alcool sera modeste, à seulement {alcohol} litres par habitant."
    else:
        description += (
            f"La consommation d'alcool sera de {alcohol} litres par habitant."
        )

    return description
