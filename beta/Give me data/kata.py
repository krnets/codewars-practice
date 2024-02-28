def has_permission(user_info, accessing_data):
    any_allow = "*_allow"
    any_deny = "*_deny"
    data_allow = accessing_data + "_allow"
    data_deny = accessing_data + "_deny"

    if (data_deny in user_info) or (any_deny in user_info and data_allow not in user_info):
        return False
    return (any_allow in user_info) or (data_allow in user_info)
