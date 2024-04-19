DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Interests;
DROP TABLE IF EXISTS UserInterests;
DROP TABLE IF EXISTS Clubs;

CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE Interests (
    interestID INTEGER PRIMARY KEY,
    interestType TEXT UNIQUE NOT NULL,
    interestName TEXT UNIQUE NOT NULL
);

CREATE TABLE UserInterests (
    id INTEGER,
    interestID INTEGER,
    CONSTRAINT PK_Userinterest PRIMARY KEY (id,interestID),
    FOREIGN KEY (id) REFERENCES Users (id),
    FOREIGN KEY (interestID) REFERENCES Interests (interestID)
);

CREATE TABLE Clubs (
    clubID INTEGER PRIMARY KEY,
    clubName TEXT NOT NULL,
    description TEXT
);

CREATE TABLE ClubInterests (
    clubID INTEGER,
    interestID INTEGER,
    CONSTRAINT PK_ClubInterests PRIMARY KEY (clubID,interestID),
    FOREIGN KEY (clubID) REFERENCES Clubs (clubID),
    FOREIGN KEY (interestID) REFERENCES Interests (interestID)
);

CREATE TABLE Events (
    eventID INTEGER PRIMARY KEY,
    eventName TEXT NOT NULL,
    description TEXT,
    date DATE,
    clubID INTEGER,
    FOREIGN KEY (clubID) REFERENCES Clubs (clubID)
);