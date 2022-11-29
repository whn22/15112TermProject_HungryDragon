        NFdashLeft = '002_nf_Dash.png'
        dashL = app.loadImage(NFdashLeft)
        dashL = app.scaleImage(dashL, 0.6)
        for i in range(13):
            sprite = dashL.crop((52*i, 0, 52+52*i, 170))
            # sprite = idleL.crop((61*i, 0, 60+61*i, 190))
            for j in range(4):
                self.dashLeft.append(sprite)
        dashR = dashL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(13):
            sprite = dashR.crop((52*i, 0, 52+52*i, 170))
            # sprite = idleR.crop((61*i, 0, 60+61*i, 190))
            for j in range(4):
                self.dashRight.append(sprite)