class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class GeneratorVert:
    def __init__(self, l, h, d, lc, rc):
        self.points = []
        self.edges = []
        self.l = l
        self.h = h
        self.d = d
        self.lc = lc
        self.rc = rc
        self.W = 0.25

    def generator_vertices(self):
        self.points.append(Point(0, 0, self.W))
        self.points.append(Point(0, 0, -self.W))
        self.points.append(Point(self.l - 4.5 * self.lc, 0, self.W))
        self.points.append(Point(self.l - 4.5 * self.lc, 0, -self.W))
        self.points.append(Point(self.l - 3.5 * self.lc, 0, self.W))
        self.points.append(Point(self.l - 3.5 * self.lc, 0, -self.W))
        self.points.append(Point(self.l - 2.5 * self.lc, 0, self.W))
        self.points.append(Point(self.l - 2.5 * self.lc, 0, -self.W))
        self.points.append(Point(self.l - 1.5 * self.lc, 0, self.W))
        self.points.append(Point(self.l - 1.5 * self.lc, 0, -self.W))
        self.points.append(Point(self.l, 0, self.W))
        self.points.append(Point(self.l, 0, -self.W))
        self.points.append(Point(self.l, self.h, self.W))
        self.points.append(Point(self.l, self.h, -self.W))
        self.points.append(Point(self.l - 1.5 * self.lc, self.h, self.W))
        self.points.append(Point(self.l - 1.5 * self.lc, self.h, -self.W))
        self.points.append(Point(self.l - 2.5 * self.lc, self.h, self.W))
        self.points.append(Point(self.l - 2.5 * self.lc, self.h, -self.W))
        self.points.append(Point(self.l - 3.5 * self.lc, self.h, self.W))
        self.points.append(Point(self.l - 3.5 * self.lc, self.h, -self.W))
        self.points.append(Point(self.l - 4.5 * self.lc, self.h, self.W))
        self.points.append(Point(self.l - 4.5 * self.lc, self.h, -self.W))
        self.points.append(Point(0, self.h, self.W))
        self.points.append(Point(0, self.h, -self.W))

        self.points.append(Point(self.l - 4 * self.lc - self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 4 * self.lc - self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 4 * self.lc + self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 4 * self.lc + self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 4 * self.lc - self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 4 * self.lc - self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 4 * self.lc + self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 4 * self.lc + self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 -self.W))

        self.points.append(Point(self.l - 3 * self.lc - self.d / (2 * 1.414), self.rc - self.d / (2 * 1.414), self.W))
        self.points.append(Point(self.l - 3 * self.lc - self.d / (2 * 1.414), self.rc - self.d / (2 * 1.414), -self.W))
        self.points.append(Point(self.l - 3 * self.lc + self.d / (2 * 1.414), self.rc - self.d / (2 * 1.414), self.W))
        self.points.append(Point(self.l - 3 * self.lc + self.d / (2 * 1.414), self.rc - self.d / (2 * 1.414), -self.W))
        self.points.append(Point(self.l - 3 * self.lc - self.d / (2 * 1.414), self.rc + self.d / (2 * 1.414), self.W))
        self.points.append(Point(self.l - 3 * self.lc - self.d / (2 * 1.414), self.rc + self.d / (2 * 1.414), -self.W))
        self.points.append(Point(self.l - 3 * self.lc + self.d / (2 * 1.414), self.rc + self.d / (2 * 1.414), self.W))
        self.points.append(Point(self.l - 3 * self.lc + self.d / (2 * 1.414), self.rc + self.d / (2 * 1.414), -self.W))

        self.points.append(Point(self.l - 2 * self.lc - self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 2 * self.lc - self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 2 * self.lc + self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 2 * self.lc + self.d / (2 * 1.414), self.h - self.rc - self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 2 * self.lc - self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 2 * self.lc - self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 -self.W))
        self.points.append(Point(self.l - 2 * self.lc + self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 self.W))
        self.points.append(Point(self.l - 2 * self.lc + self.d / (2 * 1.414), self.h - self.rc + self.d / (2 * 1.414),
                                 -self.W))

    def generator_edges(self):
        self.edges.append(Point(self.l - 4 * self.lc, self.h - self.rc + self.d / 2, self.W))
        self.edges.append(Point(self.l - 4 * self.lc, self.h - self.rc + self.d / 2, -self.W))
        self.edges.append(Point(self.l - 4 * self.lc + self.d / 2, self.h - self.rc, self.W))
        self.edges.append(Point(self.l - 4 * self.lc + self.d / 2, self.h - self.rc, -self.W))
        self.edges.append(Point(self.l - 4 * self.lc, self.h - self.rc - self.d / 2, self.W))
        self.edges.append(Point(self.l - 4 * self.lc, self.h - self.rc - self.d / 2, -self.W))
        self.edges.append(Point(self.l - 4 * self.lc - self.d / 2, self.h - self.rc, self.W))
        self.edges.append(Point(self.l - 4 * self.lc - self.d / 2, self.h - self.rc, -self.W))

        self.edges.append(Point(self.l - 3 * self.lc, self.rc + self.d / 2, self.W))
        self.edges.append(Point(self.l - 3 * self.lc, self.rc + self.d / 2, -self.W))
        self.edges.append(Point(self.l - 3 * self.lc + self.d / 2, self.rc, self.W))
        self.edges.append(Point(self.l - 3 * self.lc + self.d / 2, self.rc, -self.W))
        self.edges.append(Point(self.l - 3 * self.lc, self.rc - self.d / 2, self.W))
        self.edges.append(Point(self.l - 3 * self.lc, self.rc - self.d / 2, -self.W))
        self.edges.append(Point(self.l - 3 * self.lc - self.d / 2, self.rc, self.W))
        self.edges.append(Point(self.l - 3 * self.lc - self.d / 2, self.rc, -self.W))

        self.edges.append(Point(self.l - 2 * self.lc, self.h - self.rc + self.d / 2, self.W))
        self.edges.append(Point(self.l - 2 * self.lc, self.h - self.rc + self.d / 2, -self.W))
        self.edges.append(Point(self.l - 2 * self.lc + self.d / 2, self.h - self.rc, self.W))
        self.edges.append(Point(self.l - 2 * self.lc + self.d / 2, self.h - self.rc, -self.W))
        self.edges.append(Point(self.l - 2 * self.lc, self.h - self.rc - self.d / 2, self.W))
        self.edges.append(Point(self.l - 2 * self.lc, self.h - self.rc - self.d / 2, -self.W))
        self.edges.append(Point(self.l - 2 * self.lc - self.d / 2, self.h - self.rc, self.W))
        self.edges.append(Point(self.l - 2 * self.lc - self.d / 2, self.h - self.rc, -self.W))

    def points_to_string(self):
        export = ""
        for i, point in enumerate(self.points):
            export += f"    ({point.x} {point.y} {point.z}) //{i}\n"
        return export

    def edges_to_string(self):
        return (
                f"  arc 28 30 ({self.edges[0].x} {self.edges[0].y} {self.edges[0].z})\n" +
                f"  arc 29 31 ({self.edges[1].x} {self.edges[1].y} {self.edges[1].z})\n" +
                f"  arc 26 30 ({self.edges[2].x} {self.edges[2].y} {self.edges[2].z})\n" +
                f"  arc 27 31 ({self.edges[3].x} {self.edges[3].y} {self.edges[3].z})\n" +
                f"  arc 24 26 ({self.edges[4].x} {self.edges[4].y} {self.edges[4].z})\n" +
                f"  arc 25 27 ({self.edges[5].x} {self.edges[5].y} {self.edges[5].z})\n" +
                f"  arc 24 28 ({self.edges[6].x} {self.edges[6].y} {self.edges[6].z})\n" +
                f"  arc 25 29 ({self.edges[7].x} {self.edges[7].y} {self.edges[7].z})\n" +
                f"  arc 36 38 ({self.edges[8].x} {self.edges[8].y} {self.edges[8].z})\n" +
                f"  arc 37 39 ({self.edges[9].x} {self.edges[9].y} {self.edges[9].z})\n" +
                f"  arc 34 38 ({self.edges[10].x} {self.edges[10].y} {self.edges[10].z})\n" +
                f"  arc 35 39 ({self.edges[11].x} {self.edges[11].y} {self.edges[11].z})\n" +
                f"  arc 32 34 ({self.edges[12].x} {self.edges[12].y} {self.edges[12].z})\n" +
                f"  arc 33 35 ({self.edges[13].x} {self.edges[13].y} {self.edges[13].z})\n" +
                f"  arc 32 36 ({self.edges[14].x} {self.edges[14].y} {self.edges[14].z})\n" +
                f"  arc 33 37 ({self.edges[15].x} {self.edges[15].y} {self.edges[15].z})\n" +
                f"  arc 44 46 ({self.edges[16].x} {self.edges[16].y} {self.edges[16].z})\n" +
                f"  arc 45 47 ({self.edges[17].x} {self.edges[17].y} {self.edges[17].z})\n" +
                f"  arc 42 46 ({self.edges[18].x} {self.edges[18].y} {self.edges[18].z})\n" +
                f"  arc 43 47 ({self.edges[19].x} {self.edges[19].y} {self.edges[19].z})\n" +
                f"  arc 40 42 ({self.edges[20].x} {self.edges[20].y} {self.edges[20].z})\n" +
                f"  arc 41 43 ({self.edges[21].x} {self.edges[21].y} {self.edges[21].z})\n" +
                f"  arc 40 44 ({self.edges[22].x} {self.edges[22].y} {self.edges[22].z})\n" +
                f"  arc 41 45 ({self.edges[23].x} {self.edges[23].y} {self.edges[23].z})\n"
        )

