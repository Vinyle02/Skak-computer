

pst = {
    #For pieces on bottom
    'Pawn': (   0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
             0,   0,   0,   0,   0,   0,   0,   0),
    'Knight': ( -66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69),
    'Bishop': ( -59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10),
    'Rook': (  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32),
    'Queen': (   6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42),
    'King': (   4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18),
}

pst2 = {
"Pawn": (0, 0, 0, 0, 0, 0, 0, 0,
         -31, 3, -14, -36, -37, -7, 8, -31,
         -19, 3, -2, -10, -11, 5, 9, -22,
         -23, 0, 1, 6, 9, 10, 3, -26,
         -13, 15, 0, 14, 15, -2, 16, -17,
         7, 44, 31, 40, 44, 21, 29, 7,
         90, 85, 82, 102, 73, 86, 83, 78,
         0, 0, 0, 0, 0, 0, 0, 0),
"Knight": (-69, -22, -35, -19, -24, -26, -23, -74, -20, -23, 0, 2, 0, 2, -15, -23, -14, 11, 15, 18, 22, 13, 10, -18, 0, 2, 35, 22, 21, 31, 5, -1, 17, 25, 41, 33, 37, 45, 24, 24, -2, 62, 27, 73, 74, 1, 67, 10, -14, -4, 62, 4, -36, 100, -6, -3, -70, -58, -55, -10, -75, -75, -53, -66),
"Bishop": (-10, -10, -15, -14, -12, -15, 2, -7, 16, 20, 6, 7, 6, 11, 20, 19, 15, 20, 25, 8, 15, 24, 25, 14, 7, 0, 16, 17, 23, 17, 10, 13, 10, 15, 25, 26, 34, 20, 17, 25, -14, 28, -10, 52, 41, -32, 39, -9, -22, 2, 31, -39, -42, 35, 20, -11, -50, -37, -107, -23, -76, -82, -78, -59),
"Rook":(-32, -31, -18, -2, 5, -18, -24, -30, -53, -44, -43, -29, -26, -31, -38, -53, -46, -26, -35, -25, -25, -42, -28, -42, -30, -46, -29, -13, -21, -16, -35, -28, -6, -9, -4, 18, 13, 16, 5, 0, 15, 25, 27, 45, 33, 28, 35, 19, 60, 34, 62, 55, 67, 56, 29, 55, 50, 56, 33, 37, 4, 33, 29, 35),
"Queen": (-42, -34, -36, -31, -13, -31, -30, -39, -38, -21, -15, -15, -19, 0, -18, -36, -27, -16, -11, -16, -11, -13, -6, -30, -22, -20, -10, -1, -5, -2, -15, -14, -6, -13, 20, 25, 17, 22, -16, 1, 2, 43, 63, 72, 60, 32, 43, -2, 24, 57, 76, 20, -10, 60, 32, 14, 26, 88, 24, 69, -104, -8, 1, 6),
"King": (18, 40, -1, 6, -14, -3, 30, 17, 4, 13, -18, -57, -50, -14, 3, -4, -32, -29, -32, -64, -79, -43, -42, -47, -50, -8, -47, -51, -28, -52, -43, -55, -49, 0, 13, -19, -4, 11, 50, -55, -31, 37, 28, -67, 44, -57, 12, -62, 3, 10, 55, 56, 56, 55, 10, -32, -62, 83, 60, -99, -99, 47, 54, 4)
}
