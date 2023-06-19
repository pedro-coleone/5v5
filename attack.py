def att_stg_5v5(self):
        """Input: None
        Description: Attack strategy to 5v5, 2 defenders follow a semi circle where the ball is projected,
                     3 attakers chase the ball.
        Output: None."""
        ball_coordinates_x, ball_coordinates_y = self.ball.get_coordinates()
        dist = sqrt((ball_coordinates_x - self.their_goal_x) ** 2 + (ball_coordinates_y - self.their_goal_y) ** 2)

        up_corner_y = 180
        down_corner_y = 0
        
        if self.radius is None:
            self.radius = identify_radius.estimate_radius(self.enemy_robots, self.their_goal_x, self.their_goal_y)
        else:
            self.radius = (identify_radius.estimate_radius(self.enemy_robots, self.their_goal_x, self.their_goal_y) + self.radius) / 2
        
        self.radius = 37.5

        # Robôs 0 e 1 mantém-se na defese
        # Robôs 2, 3 e 4 vão para o ataque
        max_angle = math.pi / 6

        # Calculates angle between ball, goal's center and field borders
        if ball_coordinates_y > self.their_goal_y:
            ball_angle = math_aux.angle_between_pair_lines(ball_coordinates_x, ball_coordinates_y, self.their_goal_x, up_corner_y, self.their_goal_x, self.their_goal_y)
        else:
            ball_angle = math_aux.angle_between_pair_lines(ball_coordinates_x, ball_coordinates_y, self.their_goal_x, down_corner_y, self.their_goal_x, self.their_goal_y)
        print(f"---> Angle between ball an enemy goal = {ball_angle}")

        # Marks deffence depending on the angle value
        if ball_angle < max_angle and self.marking_count < 120:
            
            if not self.mray and ball_coordinates_x > 125:
                action.marking_their_deffence(self.robots[4], self.their_goal_x - self.radius, self.their_goal_y, self.marking_count)
            elif ball_coordinates_x < 125:
                action.marking_their_deffence(self.robots[4], self.their_goal_x + self.radius, self.their_goal_y, self.marking_count)

            self.two_attackers(2, 3, 'default')

        else:

            self.marking_count = 0                        
            self.three_attackers(2, 3, 4, '2 leaders')
        
        action.screenOutBall(self.robots[0], self.ball, 20, leftSide=not self.mray, upperLim=110, lowerLim=70)
        action.screenOutBall(self.robots[1], self.ball, 90, leftSide=not self.mray, upperLim=180, lowerLim=0)

def goal_distance(robot, our_goal_x, our_goal_y):

    dist = math.sqrt((robot.xPos - our_goal_x) ** 2 + (robot.yPos - our_goal_y) ** 2)
    return dist

def estimate_radius(enemy_robots, their_goal_x, their_goal_y):

    distances = []
    for robot in enemy_robots:
        dist = goal_distance(robot, their_goal_x, their_goal_y)
        distances.append(dist)
    
    distances.sort()
    
    radius1 = distances[1]
    radius2 = distances[2]
    
    radius = (radius1 + radius2) / 2

    return radius

def angle_between_pair_lines(point1_x, point1_y, point2_x, point2_y, intersection_point_x, intersection_point_y):
    """Input: Three pair of points that defines a pair of lines intersecting.
    Description: Calculates the smaller angle between the pair of lines.
    Output: Smaller angle between the pair of lines."""
    point1_x -= intersection_point_x * -1
    point1_y -= intersection_point_y
    point2_x -= intersection_point_x * -1
    point2_y -= intersection_point_y
    
    m1 = point1_y / (0.001 if point1_x == 0 else point1_x)
    m2 = point2_y / (0.001 if point2_x == 0 else point2_x)

    # theta = atan((m1 - m2) / (1 + m1 * m2))
    theta = abs(atan(m1))

    return theta

def two_attackers(self, id_robot1, id_robot2, strategy = 'default'):
        """Input: IDs of the 2 attackers.
        Description: Attack strategy to 5v5 with 2 attackers (follower and leader).
        Output: None."""
        action.followLeader(self.robots[0], self.robots[2], self.robots[3], self.ball,
                            self.enemy_robots[0], self.enemy_robots[1], self.enemy_robots[2], self.enemy_robots[3], self.enemy_robots[4])
    
def three_attackers(self, id_robot1, id_robot2, id_robot3, strategy = '1 leader'):
    """Input: IDs of the 3 attackers and attack strategy.
    Description: Attack strategy to 5v5 with 3 attackers between 3 different options.
    Output: None."""

    # print(f"Strategy used: {strategy}")

    match strategy:
        case '3 leaders':
            action.attack_3_leaders(self.ball, self.robots[id_robot1], self.robots[id_robot2], self.robots[id_robot3], self.mray, self.enemy_robots)
        case '2 leaders':
            action.attack_2_leaders(self.ball, self.robots[id_robot1], self.robots[id_robot2], self.robots[id_robot3], self.mray, self.enemy_robots)
        case '1 leader':
            action.attack_1_leaders(self.ball, self.robots[id_robot1], self.robots[id_robot2], self.robots[id_robot3], self.mray, self.enemy_robots)
        case _:
            print("Strategy is not defined, hence using default strategy, i.e., 3 leaders).")
            action.attack_3_leaders(self.ball, self.robots[id_robot1], self.robots[id_robot2], self.robots[id_robot3], self.mray, self.enemy_robots)
