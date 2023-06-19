def marking_their_deffence(robot, marking_point_x, marking_point_y, marking_count):
    """Input: Robot's ID that will mark the enemy deffence
    Description: Robot will block the deffence movimentation.
    Output: None."""
    print("---> Marking enemy deffence. <---")
    marking_count += 1

    robot.target.update(marking_point_x, marking_point_y, pi)

    v, w = univecController(robot, robot.target, avoidObst=False, n=16, d=2, stopWhenArrive=True)

    robot.simSetVel(v,w)

def attack_3_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: All 3 attackers act like leaders, trying to shoot ball to the goal.
    Output: None."""
    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])

def attack_2_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: 2 robots act like leaders and the other follow the leader that's closest to the ball.
    Output: None."""
    select_2_leaders(robot0, robot1, robot2, ball)

    if robot2.isLeader and robot1.isLeader:
        robots_leaders = [robot2, robot1]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot0.dist(ball) < 40:
                if (robot2.xPos > 195 and 100 > robot2.yPos > 40) and (robot1.xPos > 195 and 100 > robot1.yPos > 40):
                    follower_2(robot0, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot0, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

        # Same idea but for the other side of de field
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=mray, friend1=robot1, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot1, ball, left_side=mray, friend1=robot2, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])

            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot0.dist(ball) < 40:
                if (robot2.xPos < 35 and 100 > robot2.yPos > 40) and (robot1.xPos < 35 and 100 > robot1.yPos > 40):
                    follower_2(robot0, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot0, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

    elif robot2.isLeader and robot0.isLeader:
        robots_leaders = [robot2, robot1]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot2, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot1.dist(ball) < 40:
                if (robot2.xPos > 195 and 100 > robot2.yPos > 40) and (robot1.xPos > 195 and 100 > robot1.yPos > 40):
                    follower_2(robot1, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot1, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot2, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot1.dist(ball) < 40:
                if (robot2.xPos < 35 and 100 > robot2.yPos > 40) and (robot0.xPos < 35 and 100 > robot0.yPos > 40):
                    follower_2(robot1, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot1, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

    else:
        robots_leaders = [robot1, robot0]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot2.dist(ball) < 40:
                if (robot1.xPos > 195 and 100 > robot1.yPos > 40) and (robot0.xPos > 195 and 100 > robot0.yPos > 40):
                    follower_2(robot2, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot2, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot2.dist(ball) < 40:
                if (robot1.xPos < 35 and 100 > robot1.yPos > 40) and (robot0.xPos < 35 and 100 > robot0.yPos > 40):
                    follower_2(robot2, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot2, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

    return

def attack_1_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: 1 robot acts like leaders and the other 2 follow it.
    Output: None."""
    leaderSelector(robot1, robot2, ball)

    if robot2.isLeader:
        if not mray:
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            '''
            If is the robot 1 is close enough to the tha ball, starts to do the defender spin
            '''
            if robot1.dist(ball) < 40:
                if robot2.xPos > 195 and (100 > robot2.yPos > 40):
                    follower(robot1, robot2, ball, robot0)
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot2, ball, robot0)
            
            if robot0.dist(ball) < 40:
                if robot2.xPos > 195 and (100 > robot2.yPos > 40):
                    follower(robot0, robot2, ball, robot0)
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot2, ball, robot0)

        #Same Idea but for the other side of de field
        else:
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot2.xPos < 35 and (100 > robot2.yPos > 40):
                    follower(robot1, robot2, ball, robot0)
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot2, ball, robot0)

            if robot0.dist(ball) < 40:
                if robot2.xPos < 35 and (100 > robot2.yPos > 40):
                    follower(robot0, robot2, ball, robot0)
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot2, ball, robot0)

    elif robot1.isLeader:
        if not mray:
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot0.dist(ball) < 40:
                if robot1.xPos > 195 and (100 > robot1.yPos > 40):
                    follower(robot0, robot1, ball, robot0)
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot1, ball, robot2)

            if robot2.dist(ball) < 40:
                if robot1.xPos > 195 and (100 > robot1.yPos > 40):
                    follower(robot2, robot1, ball, robot0)
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot1, ball, robot0)
            
        else:
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot0.dist(ball) < 40:
                if robot1.xPos < 35 and (100 > robot1.yPos > 40):
                    follower(robot0, robot1, ball, robot0)
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot1, ball, robot2)
            
            if robot2.dist(ball) < 40:
                if robot1.xPos < 35 and (100 > robot1.yPos > 40):
                    follower(robot2, robot1, ball, robot0)
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot1, ball, robot0)
    
    else:
        if not mray:
            defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot0.xPos > 195 and (100 > robot0.yPos > 40):
                    follower(robot1, robot0, ball, robot2)
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot0, ball, robot2)

            if robot2.dist(ball) < 40:
                if robot0.xPos > 195 and (100 > robot0.yPos > 40):
                    follower(robot2, robot0, ball, robot1)
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot0, ball, robot1)
            
        else:
            defenderSpin(robot0, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot0.xPos < 35 and (100 > robot0.yPos > 40):
                    follower(robot1, robot0, ball, robot2)
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot0, ball, robot2)
            
            if robot2.dist(ball) < 40:
                if robot0.xPos < 35 and (100 > robot0.yPos > 40):
                    follower(robot2, robot0, ball, robot1)
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot0, ball, robot1)

    return

def select_1_leader(robot1, robot2, robot3, ball):
    """Input: 3 robot attackers and the ball.
    Description: Selects one among the attackers as the leader.
    Output: None."""

    '''
    Calculate the distan of both robots to the ball
    '''
    dist1 = sqrt((robot1.xPos - ball.xPos) ** 2 + (robot1.yPos - ball.yPos) ** 2)
    dist2 = sqrt((robot2.xPos - ball.xPos) ** 2 + (robot2.yPos - ball.yPos) ** 2)
    dist3 = sqrt((robot3.xPos - ball.xPos) ** 2 + (robot3.yPos - ball.yPos) ** 2)

    if dist3 < dist2 and dist3 < dist1: # Strategy if robot 3 is closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot1.isLeader = False
            robot2.isLeader = False
            robot3.holdLeader += 1

        elif robot3.isLeader:
            robot3.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot3.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot3.holdLeader += 1
        
        elif robot2.holdLeader > 60:
            robot3.isLeader = True
            robot2.isLeader = False
            robot2.holdLeader = 0
            robot3.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        else:
            robot2.holdLeader += 1

    # Same idea, but robot 2 is closer to the ball
    elif dist2 < dist1 and dist2 < dist3: # Strategy if robot 2 is closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot2.isLeader = True
            robot1.isLeader = False
            robot3.isLeader = False
            robot2.holdLeader += 1

        elif robot2.isLeader:
            robot2.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot2.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot2.holdLeader += 1
        
        elif robot3.holdLeader > 60:
            robot2.isLeader = True
            robot3.isLeader = False
            robot3.holdLeader = 0
            robot2.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        else:
            robot3.holdLeader += 1

    # Same idea, but robot 1 is closer to the ball
    else:
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot1.isLeader = True
            robot2.isLeader = False
            robot3.isLeader = False
            robot1.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        elif robot2.holdLeader > 60:
            robot1.isLeader = True
            robot2.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader = 0
        
        elif robot3.holdLeader > 60:
            robot1.isLeader = True
            robot3.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader = 0

        elif robot2.isLeader:
            robot2.holdLeader += 1

        else:
            robot3.holdLeader += 1

def select_2_leaders(robot1, robot2, robot3, ball): # ok
    """Input: 3 robot attackers and the ball.
    Description: Selects two among the attackers as the leaders.
    Output: None."""

    '''
    Calculate the distan of both robots to the ball
    '''
    dist1 = sqrt((robot1.xPos - ball.xPos) ** 2 + (robot1.yPos - ball.yPos) ** 2)
    dist2 = sqrt((robot2.xPos - ball.xPos) ** 2 + (robot2.yPos - ball.yPos) ** 2)
    dist3 = sqrt((robot3.xPos - ball.xPos) ** 2 + (robot3.yPos - ball.yPos) ** 2)

    if dist3 < dist1 and dist2 < dist1: # Strategy if robot 3 and 2 are closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot2.isLeader = True
            robot1.isLeader = False
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        elif robot3.isLeader and robot2.isLeader:
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot3.isLeader = True
            robot2.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        else:
            robot1.holdLeader += 1

            if robot2.holdLeader > 60:                
                robot3.isLeader = True
                robot2.isLeader = False                
                robot2.holdLeader = 0
                robot3.holdLeader += 1

            elif robot3.holdLeader > 60:
                robot2.isLeader = True
                robot3.isLeader = False                
                robot3.holdLeader = 0
                robot2.holdLeader += 1

            elif robot2.isLeader:
                robot2.holdLeader += 1
            
            else:
                robot3.holdLeader += 1

    # Same idea, but robots 3 and 1 are closer to the ball
    elif dist3 < dist2 and dist1 < dist2: # Strategy if robots 3 and 1 are closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot1.isLeader = True
            robot2.isLeader = False
            robot3.holdLeader += 1
            robot1.holdLeader += 1

        elif robot3.isLeader and robot1.isLeader:
            robot3.holdLeader += 1
            robot1.holdLeader += 1

        elif robot2.holdLeader > 60:
            robot3.isLeader = True
            robot1.isLeader = True
            robot2.isLeader = False
            robot2.holdLeader = 0
            robot1.holdLeader += 1
            robot3.holdLeader += 1

        else:
            robot2.holdLeader += 1

            if robot1.holdLeader > 60:                
                robot3.isLeader = True
                robot1.isLeader = False
                robot1.holdLeader = 0
                robot3.holdLeader += 1

            elif robot3.holdLeader > 60:
                robot1.isLeader = True
                robot3.isLeader = False                
                robot3.holdLeader = 0
                robot1.holdLeader += 1

            elif robot1.isLeader:
                robot1.holdLeader += 1
            
            else:
                robot3.holdLeader += 1

    # Same idea, but robots 1 and 2 are closer to the ball
    else:
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot1.isLeader = True
            robot2.isLeader = True
            robot3.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader += 1

        elif robot1.isLeader and robot2.isLeader:
            robot1.holdLeader += 1
            robot2.holdLeader += 1

        elif robot3.holdLeader > 60:
            robot1.isLeader = True
            robot2.isLeader = True
            robot3.isLeader = False
            robot3.holdLeader = 0
            robot2.holdLeader += 1
            robot1.holdLeader += 1

        else:
            robot3.holdLeader += 1

            if robot1.holdLeader > 60:                
                robot2.isLeader = True
                robot1.isLeader = False
                robot1.holdLeader = 0
                robot2.holdLeader += 1

            elif robot2.holdLeader > 60:
                robot1.isLeader = True
                robot2.isLeader = False                
                robot2.holdLeader = 0
                robot1.holdLeader += 1

            elif robot1.isLeader:
                robot1.holdLeader += 1
            
            else:
                robot2.holdLeader += 1
    
    # print("------------------------------")
    # print(f"Robot 3 is {'' if robot3.isLeader else 'not '} a leader.")
    # print(f"Robot 3 hold for {robot3.holdLeader} seconds.")
    # print(f"Robot 2 is {'' if robot2.isLeader else 'not '} a leader.")
    # print(f"Robot 2 hold for {robot2.holdLeader} seconds.")
    # print(f"Robot 1 is {'' if robot1.isLeader else 'not '} a leader.")
    # print(f"Robot 1 hold for {robot1.holdLeader} seconds.")
    # print("------------------------------")

def select_3_leaders(robot1, robot2, robot3, ball):
    """Input: 3 robot attackers and the ball.
    Description: Selects all the attackers as leaders.
    Output: None."""
    robot1.isLeader = True
    robot2.isLeader = True
    robot3.isLeader = True

def follower_2(robot_follower, robots_leaders, ball, robot_enemy_0=None, robot_enemy_1=None, robot_enemy_2=None, robot_enemy_3=None, robot_enemy_4=None):
    """Input: Follower robot, leaders robots, ball and 4 enemy robots.
    Description: Follower follows the leaders that's more close to the ball.
    Output: None."""

    '''
    Defines the position of the follower based on the leader position, the position is a diagonal
    projection of leader position.
    '''
    dist0 = sqrt((robots_leaders[0].xPos - ball.xPos) ** 2 + (robots_leaders[0].yPos - ball.yPos) ** 2)
    dist1 = sqrt((robots_leaders[1].xPos - ball.xPos) ** 2 + (robots_leaders[1].yPos - ball.yPos) ** 2)

    if dist0 < dist1:
        robot_leader = robots_leaders[0]
        other_leader = robots_leaders[1]
    else:
        robot_leader = robots_leaders[1]
        other_leader = robots_leaders[0]

    if robot_leader.yPos > 90:
        if robot_leader.xPos > 126:
            proj_x = robot_leader.xPos - 15
            proj_y = robot_leader.yPos - 30
        else:
            proj_x = robot_leader.xPos + 15
            proj_y = robot_leader.yPos - 15
    else:
        if robot_leader.xPos > 126:
            proj_x = robot_leader.xPos - 15
            proj_y = robot_leader.yPos + 30
        else:
            proj_x = robot_leader.xPos + 15
            proj_y = robot_leader.yPos + 15
    '''
    Calculate distante between the follower and the projected point
    '''
    dist = sqrt((robot_follower.xPos - proj_x) ** 2 + (robot_follower.yPos - proj_y) ** 2)
    arrival_theta = arctan2(ball.yPos - robot_follower.yPos, ball.xPos - robot_follower.xPos)
    robot_follower.target.update(proj_x, proj_y, arrival_theta)

    if dist < 10: # Check if the robot is close to the projected point and stops the robot
        stop(robot_follower)
    else:
        # No friends to avoid
        if (other_leader is None) and (robot_enemy_0 is None) and (robot_enemy_1 is None) and (robot_enemy_2 is None) and (robot_enemy_3 is None) and (robot_enemy_4 is None):
            v, w = univecController(robot_follower, robot_follower.target, avoid_obst=False, n=16, d=2)
        else:  # Both friends to avoid
            robot_follower.obst.update2(robot_follower, ball, other_leader, robot_leader, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
            v, w = univecController(robot_follower, robot_follower.target, True, robot_follower.obst, n=4, d=4)

        robot_follower.simSetVel(v, w)

def follow_leader_to_quadrant(robot0, robot1, robot2, ball, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4):
    """Input: 3 robot attackers, ball and 4 enemy robots.
    Description: Guide the robots to the other quadrant of the field.
    Output: None."""

    leaderSelector(robot1, robot2, ball)

    if robot2.isLeader:
        if not robot1.teamYellow:
            defenderSpin(robot2, ball, left_side=not robot2.teamYellow, friend1=robot0, friend2=robot0,
                              enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
            '''
            If is the robot 1 is close enough to the tha ball, starts to do the defender spin
            '''
            if robot1.dist(ball) < 40:
                if robot2.xPos > 195 and (100 > robot2.yPos > 40):
                    follower(robot1, robot2, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
                else:
                    defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                                    enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
            else:
                follower(robot1, robot2, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)

        #Same Idea but for the other side of de field
        else:
            if ball.xPos > 195 and (120 > ball.yPos > 50):
                if robot1.xPos > 180:
                    screenOutBall(robot2, robot2, 55, leftSide=not robot2.teamYellow, upper_lim=120, lower_lim=10)
                else:
                    screenOutBall(robot2, ball, 55, leftSide=not robot2.teamYellow, upper_lim=120, lower_lim=10)
                follower(robot1, robot2, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)

            else:
                defenderSpin(robot2, ball, left_side=not robot2.teamYellow, friend1=robot0, friend2=robot0,
                  enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                if robot1.dist(ball) < 40:
                    if robot2.xPos < 35 and (100 > robot2.yPos > 40):
                        follower(robot1, robot2, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3,robot_enemy_4)
                    else:
                        defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                                      enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                else:
                    follower(robot1, robot2, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)

    elif robot1.isLeader:
        if not robot1.teamYellow:
            if ball.xPos < 35 and (120 > ball.yPos > 50):
                if robot1.xPos < 35:
                    screenOutBall(robot1, robot1, 55, leftSide=not robot1.teamYellow, upper_lim=120, lower_lim=10)
                else:
                    screenOutBall(robot1, ball, 55, leftSide=not robot1.teamYellow, upper_lim=120, lower_lim=10)
                follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)

            else:
                defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot0,
                              enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                if robot2.dist(ball) < 40:
                    if robot1.xPos > 195 and (100 > robot1.yPos > 40):
                        follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
                    else:
                        defenderSpin(robot2, ball, left_side=not robot2.teamYellow, friend1=robot0, friend2=robot1,
                                      enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                else:
                    follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
        else:
            if ball.xPos > 195 and (130 > ball.yPos > 50):
                if robot1.xPos > 130:
                    screenOutBall(robot1, robot1, 55, leftSide=not robot1.teamYellow, upper_lim=120, lower_lim=10)
                else:
                    screenOutBall(robot1, ball, 55, leftSide=not robot1.teamYellow, upper_lim=120, lower_lim=10)
                follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)

            else:
                defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot0,
                              enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                if robot2.dist(ball) < 40:
                    if robot1.xPos < 35 and (100 > robot1.yPos > 40):
                        follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
                    else:
                        defenderSpin(robot2, ball, left_side=not robot2.teamYellow, friend1=robot0, friend2=robot1,
                                      enemy1=robot_enemy_0, enemy2=robot_enemy_1, enemy3=robot_enemy_2, enemy4=robot_enemy_3, enemy5=robot_enemy_4)
                else:
                    follower(robot2, robot1, ball, robot0, robot_enemy_0, robot_enemy_1, robot_enemy_2, robot_enemy_3, robot_enemy_4)
