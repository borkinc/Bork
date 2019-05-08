CREATE TABLE Users
(
    uid          SERIAL PRIMARY KEY,
    username     varchar(30) UNIQUE  NOT NULL,
    password     varchar(100)        NOT NULL,
    created_on   TIMESTAMPTZ         NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email        varchar(100) UNIQUE NOT NULL,
    first_name   varchar(30)         NOT NULL,
    last_name    varchar(30)         NOT NULL,
    phone_number varchar(10) UNIQUE  NOT NULL
);

CREATE TABLE Chat_Group
(
    cid        serial PRIMARY KEY,
    uid        INTEGER REFERENCES Users (uid) ON DELETE CASCADE,
    name       varchar(25) NOT NULL,
    created_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Chat_Members
(
    cid       INTEGER REFERENCES Chat_Group (cid) ON DELETE CASCADE,
    uid       INTEGER REFERENCES Users (uid),
    joined_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (cid, uid)
);

CREATE TABLE Messages
(
    mid        serial PRIMARY KEY,
    cid        INTEGER REFERENCES Chat_Group (cid) ON DELETE CASCADE,
    uid        INTEGER REFERENCES Users (uid) ON DELETE CASCADE,
    message    VARCHAR(500),
    created_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Photo
(
    pid   serial PRIMARY KEY,
    image varchar(2083) NOT NULL,
    mid   INTEGER REFERENCES Messages (mid) ON DELETE CASCADE
);

CREATE TABLE Replies
(
    replied_to INTEGER REFERENCES Messages (mid) ON DELETE CASCADE,
    reply      INTEGER REFERENCES Messages (mid) ON DELETE CASCADE,
    PRIMARY KEY (replied_to, reply)
);

CREATE TABLE Vote
(
    mid      INTEGER REFERENCES Messages (mid) ON DELETE CASCADE,
    uid      INTEGER REFERENCES Users (uid) ON DELETE CASCADE,
    voted_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    upvote   BOOLEAN     NOT NULL,
    PRIMARY KEY (mid, uid)
);

CREATE TABLE Contacts
(
    owner_id   Integer REFERENCES Users (uid) ON DELETE CASCADE,
    contact_id Integer REFERENCES Users (uid) ON DELETE CASCADE,
    first_name VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30) NOT NULL,
    PRIMARY KEY (owner_id, contact_id)

);


CREATE TABLE Hashtags_Messages
(
    hid     SERIAL PRIMARY KEY,
    hashtag VARCHAR(50),
    mid     INTEGER REFERENCES Messages (mid)
);

