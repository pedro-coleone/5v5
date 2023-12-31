import action
from numpy import *

class Strategy:
    def __init__(self, robot0, robot1, robot2, robot3, robot4, robotEnemy0, robotEnemy1, robotEnemy2, robotEnemy3, robotEnemy4, ball, mray):
        self.robot0 = robot0
        self.robot1 = robot1
        self.robot2 = robot2
        self.robot3 = robot3
        self.robot4 = robot4
        self.robotEnemy0 = robotEnemy0
        self.robotEnemy1 = robotEnemy1
        self.robotEnemy2 = robotEnemy2
        self.robotEnemy3 = robotEnemy3
        self.robotEnemy4 = robotEnemy4
        self.ball = ball
        self.mray = mray
        self.penaltyDefensive = False
        self.penaltyOffensive = False
        self.quadrant = 0

    def coach1(self):
        """"Picks a strategy depending on the status of the field"""
        # For the time being, the only statuses considered are which side of the field the ball is in
        if self.penaltyDefensive == True:
            self.penaltyModeDefensive()
        elif self.penaltyOffensive == True:
            self.penaltyModeOffensiveSpin()
        else:
            if not self.mray:
                if self.ball.xPos < 135:
                    self.wallStgDef()
                else:
                    self.wallStgAtt()
            else:
                if self.ball.xPos > 115:
                    self.wallStgDef()
                else:
                    self.wallStgAtt()

    def basicStgDef(self):
        """Basic original strategy"""
        action.screenOutBall(self.robot3, self.ball, 150, leftSide=not self.mray, upperLim=85, lowerLim=5)
        action.screenOutBall(self.robot4, self.ball, 150, leftSide=not self.mray, upperLim=175, lowerLim=95)
        if not self.mray:
            if self.ball.xPos < 40 and self.ball.yPos > 50 and self.ball.yPos < 130:
                action.defenderPenalty(self.robot0, self.ball, leftSide=not self.mray)
                action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=85, lowerLim=5)
                action.screenOutBall(self.robot2, self.ball, 55, leftSide=not self.mray, upperLim=175, lowerLim=95)
            else:
                #listRobots = [self.robot0, self.robot3, self.robot4, self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
                friends = [self.robot0, self.robot3, self.robot4]
                enemys = [self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
                action.followLeader(self.robot0, self.robot1, self.robot2, self.ball, self.robotEnemy0, self.robotEnemy1,
                            self.robotEnemy2,self.robotEnemy3,self.robotEnemy4)
                action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=110, lowerLim=70)
        else:
            if self.ball.xPos > 195 and self.ball.yPos > 50 and self.ball.yPos < 130:
                action.defenderPenalty(self.robot0, self.ball, leftSide=not self.mray)
                action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=85, lowerLim=5)
                action.screenOutBall(self.robot2, self.ball, 55, leftSide=not self.mray, upperLim=175, lowerLim=95)
            else:
                #listRobots = [self.robot0, self.robot3, self.robot4, self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
                friends = [self.robot0, self.robot3, self.robot4]
                enemys = [self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
                action.followLeader(self.robot0, self.robot1, self.robot2, self.ball, self.robotEnemy0, self.robotEnemy1,
                            self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
                action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=110, lowerLim=70)
        if ((abs(self.robot0.theta) < deg2rad(10)) or (abs(self.robot0.theta) > deg2rad(170))) and (self.robot0.xPos < 25 or self.robot0.xPos > 225):
            self.robot0.contStopped += 1
        else:
            self.robot0.contStopped = 0

    def wallStgDef(self):
        """ Wall defense using two defenders"""
        if not self.mray:
            if self.ball.xPos < 35 and self.ball.yPos > 60 and self.ball.yPos < 120:
                action.defenderPenalty(self.robot0, self.ball, leftSide=not self.mray)
            else:
                
                action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.defenderWall(self.robot1, self.robot2,self.ball, leftSide=not self.mray)
            if self.ball.xPos > 60:
                action.followLeader(self.robot0, self.robot3, self.robot4, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                    self.robotEnemy2,self.robotEnemy3,self.robotEnemy4)
            else:
                action.screenOutBall(self.robot3, self.ball, 80, leftSide=not self.mray, upperLim=85, lowerLim=5)
                action.screenOutBall(self.robot4, self.ball, 80, leftSide=not self.mray, upperLim=175, lowerLim=95)
        else:
            if self.ball.xPos > 215 and self.ball.yPos > 60 and self.ball.yPos < 120:
                action.defenderPenalty(self.robot0, self.ball, leftSide=not self.mray)
            else:
                action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.defenderWall(self.robot1, self.robot2,self.ball, leftSide=not self.mray)
            if self.ball.xPos < 190:
                action.followLeader(self.robot0, self.robot3, self.robot4, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                    self.robotEnemy2,self.robotEnemy3,self.robotEnemy4)
            else:
                action.screenOutBall(self.robot3, self.ball, 80, leftSide=not self.mray, upperLim=85, lowerLim=5)
                action.screenOutBall(self.robot4, self.ball, 80, leftSide=not self.mray, upperLim=175, lowerLim=95)
        if ((abs(self.robot0.theta) < deg2rad(10)) or (abs(self.robot0.theta) > deg2rad(170))) and (self.robot0.xPos < 25 or self.robot0.xPos > 225):
            self.robot0.contStopped += 1
        else:
            self.robot0.contStopped = 0       
        
    def basicStgAtt(self):
        """Basic alternative strategy"""
        #listRobots = [self.robot0, self.robot1, self.robot2, self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
        friends = [self.robot0, self.robot1, self.robot2]
        enemys = [self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
        action.followLeader(self.robot0, self.robot3, self.robot4, self.ball, self.robotEnemy0, self.robotEnemy1,
                            self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)

        action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
        action.screenOutBall(self.robot1, self.ball, 90, leftSide=not self.mray, upperLim=85, lowerLim=5)
        action.screenOutBall(self.robot2, self.ball, 90, leftSide=not self.mray, upperLim=175, lowerLim=95)

    def wallStgAtt(self):
        action.followLeader(self.robot0, self.robot3, self.robot4, self.ball, self.robotEnemy0, self.robotEnemy1,
        self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
        action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
        action.defenderWall(self.robot1, self.robot2,self.ball, leftSide=not self.mray)

    def breakWallStgAtt(self):
        if self.mray and self.ball.xPos < 70 and self.ball.yPos < 30 and self.quadrant != 2 or self.quadrant == 3:
            self.quadrant = 3
            action.followLeader(self.robot0, self.robot2, self.robot3, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
            action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=150, lowerLim=30)
            action.breakWall(self.robot4, self.ball, self.quadrant,self.robot0, self.robot1, self.robotEnemy0, self.robotEnemy1,
                                                                                 self.robotEnemy2, self.robotEnemy3, self.robotEnemy4,
                                                                                 leftSide=not self.mray)
        if self.mray and self.ball.xPos < 70 and self.ball.yPos > 150 and self.quadrant != 3 or self.quadrant == 2:
            self.quadrant = 2
            action.followLeader(self.robot0, self.robot2, self.robot3, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
            action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=150, lowerLim=30)
            action.breakWall(self.robot4, self.ball, self.quadrant,self.robot0, self.robot1, self.robotEnemy0, self.robotEnemy1,
                                                                                 self.robotEnemy2, self.robotEnemy3, self.robotEnemy4,
                                                                                 leftSide=not self.mray)   
        if not self.mray and self.ball.xPos > 180 and self.ball.yPos < 30 and self.quadrant != 1 or self.quadrant == 4:
            self.quadrant = 4
            action.followLeader(self.robot0, self.robot2, self.robot3, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
            action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=150, lowerLim=30)
            action.breakWall(self.robot4, self.ball, self.quadrant,self.robot0, self.robot1, self.robotEnemy0, self.robotEnemy1,
                                                                                 self.robotEnemy2, self.robotEnemy3, self.robotEnemy4,
                                                                                 leftSide=not self.mray)
        if not self.mray and self.ball.xPos > 180 and self.ball.yPos > 150 and self.quadrant != 4 or self.quadrant == 1:
            self.quadrant = 1
            action.followLeader(self.robot0, self.robot2, self.robot3, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
            action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.screenOutBall(self.robot1, self.ball, 55, leftSide=not self.mray, upperLim=150, lowerLim=30)
            action.breakWall(self.robot4, self.ball, self.quadrant,self.robot0, self.robot1, self.robotEnemy0, self.robotEnemy1,
                                                                                 self.robotEnemy2, self.robotEnemy3, self.robotEnemy4,
                                                                                 leftSide=not self.mray)
        if self.mray and self.ball.xPos > 90 or not self.mray and self.ball.xPos < 140 or self.quadrant == 0:
            self.quadrant = 0
            action.followLeader(self.robot0, self.robot3, self.robot4, self.ball, self.robotEnemy0, self.robotEnemy1,
                                                                self.robotEnemy2, self.robotEnemy3, self.robotEnemy4)
            action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray, upperLim=115, lowerLim=65)
            action.defenderWall(self.robot1, self.robot2,self.ball, leftSide=not self.mray)

    def penaltyModeDefensive(self):
        '''Strategy to defend penalty situations'''
        action.defenderPenalty(self.robot0, self.ball, leftSide=not self.mray)

        enemys = [self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
        friends = [self.robot0, self.robot2, self.robot3, self.robot4]
        action.shoot(self.robot1,self.ball,not self.mray,friends,enemys)

        friends = [self.robot0, self.robot1, self.robot3, self.robot4]
        action.shoot(self.robot2,self.ball,not self.mray,friends,enemys)

        if not self.mray:
            if self.ball.xPos >53 or self.ball.yPos < 60 or self.ball.yPos > 120:
                self.penaltyDefensive = False
        else:
            if self.ball.xPos < 182 or self.ball.yPos < 60 or self.ball.yPos > 100:
                self.penaltyDefensive = False

    def penaltyModeOffensiveSpin(self):
        '''Strategy to convert penalty offensive situations'''
        action.screenOutBall(self.robot0, self.ball, 20, leftSide=not self.mray)
        action.screenOutBall(self.robot1, self.ball, 90, leftSide=not self.mray, upperLim=85, lowerLim=5)

        enemys = [self.robotEnemy0, self.robotEnemy1, self.robotEnemy2, self.robotEnemy3, self.robotEnemy4]
        friends = [self.robot0, self.robot1, self.robot2, self.robot4]
        action.shoot(self.robot3,self.ball,not self.mray,friends,enemys)
        friends = [self.robot0, self.robot1, self.robot3, self.robot4]
        action.shoot(self.robot2,self.ball,not self.mray,friends,enemys)
        if not self.robot4.dist(self.ball) < 9:
            action.girar(self.robot4, 100, 100)
        else:
            if self.robot4.teamYellow:
                if self.robot4.yPos < 90:
                    action.girar(self.robot4, 0, 100)
                else:
                    action.girar(self.robot4, 100, 0)
            else:
                if self.robot4.yPos > 90:
                    action.girar(self.robot4, 0, 100)
                else:
                    action.girar(self.robot4, 100, 0)
        if sqrt((self.ball.xPos-self.robot4.xPos)**2+(self.ball.yPos-self.robot4.yPos)**2) > 30:
            self.penaltyOffensive = False
