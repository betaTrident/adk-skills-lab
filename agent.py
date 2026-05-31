# ---------------------------------------------------------------------------
# Assemble: Package skills into a SkillToolset
# ---------------------------------------------------------------------------
skill_toolset = SkillToolset(
    skills=[seo_skill]
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="blog_skills_agent",
    description="A blog-writing agent powered by reusable skills.",
    instruction=(
        "You are a blog-writing assistant with specialized skills.\n\n"
        "When the user asks you to write, research, or optimize a blog post:\n"
        "1. Load the relevant skill(s) to get detailed instructions\n"
        "2. Use `load_skill_resource` to access reference materials\n"
        "3. Follow the skill's step-by-step instructions\n\n"
        "Always explain which skill you're using and why."
    ),
    tools=[skill_toolset],
)