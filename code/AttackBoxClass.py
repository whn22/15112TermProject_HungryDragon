class AttackBox():
    # def createLeftSlashBox(x, y, h):
    #     return {(x, y - 15):(x - 60, y + h + 15),
    #             (x, y - 7):(x - 85, y + h + 7),
    #             (x, y):(x - 100, y + h),
    #             (x, y + 7):(x - 112, y + h - 7),
    #             (x, y + 15):(x - 120, y + h - 15)}

    # def createRightSlashBox(x, y, h):
    #     return {(x, y - 15):(x + 60, y + h + 15),
    #             (x, y - 7):(x + 85, y + h + 7),
    #             (x, y):(x + 100, y + h),
    #             (x, y + 7):(x + 112, y + h - 7),
    #             (x, y + 15):(x + 120, y + h - 15)}
    
    def createLeftSlashBox(x, y, h):
        return {(x - 60, y - 15):(60, h + 30),
                (x - 85, y - 7):(85, h + 14),
                (x - 100, y):(100, h),
                (x - 112, y + 7):(112, h - 14),
                (x - 120, y + 15):(120, h - 30)}

    def createRightSlashBox(x, y, h):
        return {(x, y - 15):(60, h + 30),
                (x, y - 7):(85, h + 14),
                (x, y):(100, h),
                (x, y + 7):(112, h - 14),
                (x, y + 15):(120, h - 30)}