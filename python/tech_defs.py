def generate_technology_script(technology):
    script_template = """#{tech}
if = {{
    limit = {{ 
        has_technology_researched = {tech}
        NOT = {{
            has_global_variable = headlines_{tech}_researched
        }}
    }}
    set_global_variable = headlines_{tech}_researched
    save_scope_as = headlines_{tech}_researcher
    every_country = {{
        limit = {{
            is_ai = no
        }}
        post_notification = headlines_tech_{tech}
    }}
}}"""
    return script_template.format(tech=technology)

def generate_scripts(technologies):
    scripts = []
    for tech in technologies:
        script = generate_technology_script(tech)
        scripts.append(script)
    return scripts

def generate_message(technology):
    script_template = """headlines_tech_{tech} = {{
    type = country
    texture = "gfx/interface/icons/notification_icons/news_tech.dds"
    group = "headlines_tech_group"
    notification_type = feed
    days = 28
    color = neutral
}}
"""
    return script_template.format(tech=technology)

def generate_messages(technologies):
    messages = []
    for tech in technologies:
        message = generate_message(tech)
        messages.append(message)
    return messages

def generate_loc(technology):
    script_template = r"""notification_headlines_tech_{tech}_tooltip:0 "#header $notification_headlines_tech_{tech}_name$#!\n$TOOLTIP_DELIMITER$\n$notification_headlines_tech_{tech}_desc$"
 notification_headlines_tech_{tech}_name:0 "#b {tech} researched #!"
 notification_headlines_tech_{tech}_desc:1 " [SCOPE.sCountry('headlines_{tech}_researcher').GetName] has invented #bold {tech} #!. #lore REPLACE_ME #!"
"""
    return script_template.format(tech=technology)

def generate_locs(technologies):
    locs = []
    for tech in technologies:
        loc = generate_loc(tech)
        locs.append(loc)
    return locs

def main():
    # Define your list of technologies
    technologies = [
        "bessemer_process",
        "crystal_glass",
        "baking_powder",
        "nitroglycerin",
        "improved_fertilizer",
        "steam_donkey",
        "dynamite",
        "steel_railway_cars",
        "rubber_mastication",
        "pumpjacks",
        "electrical_generation",
        "aniline",
        "vulcanization",
        "nitrogen_fixation",
        "mechanized_farming",
        "plastics",
        "steam_turbine",
        "combustion_engine",
        "telephone",
        "art_silk",
        "electric_railway",
        "radio",
        "pasteurization",
        "arc_welding",
        "oil_turbine",
        "compression_ignition",
        "dough_rollers",
        "rifling",
        "breech_loading_artillery",
        "repeaters",
        "modern_nursing",
        "gantry_cranes",
        "ironclad_tech",
        "handcranked_machine_gun",
        "bolt_action_rifles",
        "trench_works",
        "destroyer",
        "submarine",
        "sea_lane_strategies",
        "automatic_machine_guns",
        "dreadnought",
        "chemical_warfare",
        "military_aviation",
        "flamethrowers",
        "nco_training",
        "carrier_tech",
        "battleship_tech",
        "mobile_armor",
        "pharmaceuticals",
        "realism",
        "organized_sports",
        "quinine",
        "steel_frame_buildings",
        "mutual_funds",
        "camera",
        "socialism",
        "elevator",
        "zeppelins",
        "malaria_prevention",
        "film",
        "paved_roads",
        "antibiotics"
    ]

    # Generate scripts for the specified technologies
    scripts = generate_scripts(technologies)

    messages = generate_messages(technologies)

    locs = generate_locs(technologies)

    # Write scripts to output file
    with open('generated_technology_scripts.txt', 'w') as file:
        for script in scripts:
            file.write(script)
            file.write('\n\n')

    print(f"Generated {len(scripts)} technology scripts. Check 'generated_technology_scripts.txt'.")

    with open('generated_technology_messages.txt', 'w') as file:
        for message in messages:
            file.write(message)
            file.write('\n\n')

    print(f"Generated {len(messages)} messages. Check 'generated_technology_messages.txt'.")

    with open('generated_technology_locs.txt', 'w') as file:
        for loc in locs:
            file.write(loc)
            file.write('\n\n')

    print(f"Generated {len(locs)} locs. Check 'generated_technology_locs.txt'.")

if __name__ == "__main__":
    main()
