# def work_needed(project_minutes, free_lancers):
#     balance = project_minutes - sum(h * 60 + m for h, m in free_lancers)
#     return (
#         f"I need to work {balance // 60} hour(s) and {balance % 60} minute(s)"
#         if balance > 0
#         else "Easy Money!"
#     )

def work_needed(project_minutes, free_lancers):
    balance = project_minutes - sum(h * 60 + m for h, m in free_lancers)
    return "I need to work {} hour(s) and {} minute(s)".format(*divmod(balance, 60)) \
            if balance > 0 else "Easy Money!"