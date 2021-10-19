def isRobotBounded(self, instructions: str) -> bool:
        #Start positions
        x , y = 0, 0
        #Start direction
        direction = 'N'
        
        for i in instructions:
            if(i == 'G'):
                if direction == 'N':
                    y += 1
                elif direction == 'W':
                    x -= 1
                elif direction == 'S':
                    y -= 1
                # 'E'
                else:
                    x += 1
            elif(i == 'L'):
                if direction == 'N':
                    direction ='W'
                elif direction == 'W':
                    direction ='S'
                elif direction == 'S':
                    direction ='E'
                # 'E'
                else:
                    direction = 'N'
            # 'R'
            else:
                if direction == 'N':
                    direction ='E'
                elif direction == 'E':
                    direction ='S'
                elif direction == 'S':
                    direction ='W'
                # 'E'
                else:
                    direction = 'N'
        
        if(x==0 and y==0) or direction!='N':
            return True #circle exists
        return False