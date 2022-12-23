def check_nickname_length(nickname):
    """检查昵称长度"""
    if len(nickname) < 1 or len(nickname) > 20:
        return False
    return True


def check_password_length(password):
    """检查密码长度"""
    if len(password) < 6 or len(password) > 20:
        return False
    return True


def check_user_id_length(user_id):
    """检查用户ID长度"""
    if len(user_id) != 8:
        return False
    return True
