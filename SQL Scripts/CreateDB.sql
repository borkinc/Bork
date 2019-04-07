CREATE TABLE Users (
                       uid          SERIAL PRIMARY KEY,
                       username     varchar(30) UNIQUE  NOT NULL,
                       password     varchar(100)        NOT NULL,
                       created_on   TIMESTAMPTZ         NOT NULL DEFAULT CURRENT_TIMESTAMP,
                       email        varchar(100) UNIQUE NOT NULL,
                       first_name   varchar(30)         NOT NULL,
                       last_name    varchar(30)         NOT NULL,
                       phone_number varchar(10)         NOT NULL
);

CREATE TABLE Chat_Group (
                            cid        serial PRIMARY KEY,
                            uid        INTEGER REFERENCES Users(uid),
                            name       varchar(25) NOT NULL,
                            created_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Chat_Members (
                              cid       INTEGER REFERENCES Chat_Group(cid),
                              uid       INTEGER REFERENCES Users(uid),
                              joined_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
                              PRIMARY KEY (cid, uid)
);

CREATE TABLE Messages (
                          mid        serial PRIMARY KEY,
                          cid        INTEGER REFERENCES Chat_Group(cid),
                          uid        INTEGER REFERENCES Users(uid),
                          message    VARCHAR(500),
                          created_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Photo (
    pid serial PRIMARY KEY,
    image varchar(2083) NOT NULL,
    mid INTEGER REFERENCES Messages(mid)
);

CREATE TABLE Replies (
    replied_to INTEGER REFERENCES Messages(mid),
    reply INTEGER REFERENCES Messages(mid),
    PRIMARY KEY(replied_to, reply)
);

CREATE TABLE Vote(
                     mid      INTEGER REFERENCES Messages(mid),
                     uid      INTEGER REFERENCES Users(uid),
                     voted_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
                     upvote   BOOLEAN     NOT NULL,
                     PRIMARY KEY(mid, uid)
);

CREATE TABLE Contacts(
    owner_id Integer REFERENCES  Users(uid),
    contact_id Integer REFERENCES Users(uid),
    PRIMARY KEY(owner_id, contact_id)
);

CREATE TABLE Hashtags(
    hid SERIAL PRIMARY KEY,
    hashtag varchar(50) UNIQUE NOT NULL
);

CREATE TABLE Hashtags_Messages(
    hid INTEGER REFERENCES Hashtags(hid),
    mid INTEGER REFERENCES Messages(mid),
    PRIMARY KEY(hid, mid)
);

