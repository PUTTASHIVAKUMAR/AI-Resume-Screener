def get_skill_gap(resume_text, job_skills):

    resume_words = set(resume_text.split())
    job_words = set(job_skills.split())

    found_skills = resume_words.intersection(job_words)
    missing_skills = job_words - resume_words

    return list(found_skills), list(missing_skills)
