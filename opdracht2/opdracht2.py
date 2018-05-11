# Opdracht 2 Computer Graphics Tommie Terhoeve TI2B 0926280
class Color_converter:

    # Converts RGB to CMY
    def RGBtoCMY(self, R, G, B):
        C = 1 - R
        M = 1 - G
        Y = 1 - B
        return C, M, Y

    # Converts CMY to RGB
    def CMYtoRGB(self, C, M, Y):
        R = 1 - C
        G = 1 - M
        B = 1 - Y
        return R, G, B

    # Converts RGB to HSL
    def RGBtoHSL(self, R, G, B):
        # Puts RGB values in list to find the min and max value
        rgblist = [R, G, B]
        minvalue = min(rgblist)
        maxvalue = max(rgblist)
        L = (minvalue+maxvalue) / 2
        # No saturation if minvalue and maxvalue are equal
        if minvalue == maxvalue:
            S = 0
            H = 0
            return L, S, H
        if L < 0.5:
            S = (maxvalue-minvalue)/(maxvalue+minvalue)
        elif L >= 0.5:
            S = (maxvalue-minvalue)/(2.0-maxvalue-minvalue)
        # Calculate Hue by checking which of the 3 values is the biggest
        maxvalue_value_index = rgblist.index(max(rgblist))
        if maxvalue_value_index == 0:
            H = (G-B)/(maxvalue-minvalue)
        elif maxvalue_value_index == 1:
            H = 2.0 + (B-R)/(maxvalue-minvalue)
        elif maxvalue_value_index == 2:
            H = 4.0 + (R-G)/(maxvalue-minvalue)
        # Convert H to degrees
        H *= 60
        return H, S, L

    # Converts HSL to RGBtoCMY
    def HSLtoRGB(self, H, S, L):
        # If there is no saturation
        if S == 0:
            R = G = B = L
            return R, G, B
        # Create 2 temporary variables which make the formula easier to read
        if L < 0.5:
            temp1 = L*(1.0+S)
        elif L >= 0.5:
            temp1 = (L + S) - (L * S)
        temp2 = 2 * L - temp1
        # Convert 360 degrees to circle of 1
        H /= 360
        temporary_R = H + 0.333
        temporary_G = H
        temporary_B = H - 0.333
        templist = [temporary_R, temporary_G, temporary_B]
        finallist = []
        # Check if values are between 0 and 1
        for i in range(len(templist)):
            if templist[i] < 0:
                templist[i] += 1
            elif templist[i] > 1:
                templist[i] -= 1
        # Calculate R,G,B
        for tempcolor in templist:
            if 6*tempcolor < 1:
                finallist.append(temp2 + (temp1-temp2) * 6 * tempcolor)
            elif 2*tempcolor < 1:
                finallist.append(temp1)
            elif 3*tempcolor < 2:
                finallist.append(temp2 + (temp1-temp2) * (0.666-tempcolor) * 6)
            else:
                finallist.append(temp2)
        return finallist[0], finallist[1], finallist[2]

    # Calculates R,G,B value of 2 surfaces with different transparencies ontop of eachother
    def transparency(self, R1, G1, B1, alpha1, R2, G2, B2):
        rgb1list = [R1, G1, B1]
        rgb2list = [R2, G2, B2]
        rgbfinalist = []
        for i in range(len(rgb1list)):
            rgbfinalist.append((alpha1 * rgb1list[i]) + (1-alpha1) * rgb2list[i])
        return rgbfinalist


colorConverter = Color_converter()
print(colorConverter.RGBtoCMY(0.3, 0.2, 0.4))
print(colorConverter.CMYtoRGB(0.2, 0.6, 0.9))
print(colorConverter.RGBtoHSL(0.22, 0.35, 0.8))
print(colorConverter.HSLtoRGB(80, 0.65, 0.98))
print(colorConverter.transparency(0.67, 0.43, 0.78, 0.9, 0.65, 0.52, 0.32))
