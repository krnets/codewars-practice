def lineup_students(st):
    return sorted(st.split(), key=lambda w: (len(w), w), reverse=True)
