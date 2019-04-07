-- Inserting 10 - 15 rows to each database table for testing purposes
-- Table: Users
-- Rows: 13
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('quaoarcone', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'plover@sbcglobal.net', 'Madina', 'Bowman', '7253068397');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('argumentvowel', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'bahwi@optonline.net', 'Can', 'Wheeler', '3427340128');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('gnatwipe', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'quinn@icloud.com', 'Frankie', 'Bolton', '5063801658');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('subwaypunish', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'danneng@aol.com', 'Nabiha', 'Salas', '3945802107');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('ledwychenewman', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'matloff@aol.com', 'Zohaib', 'Swan', '4787892333');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('wombdivisive', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'library@att.net', 'Aaran', 'Sheridan', '2142503399');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('nutsnear', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'rfoley@comcast.net', 'Shelbie', 'Walters', '7664462811');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('charmsooner', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'tfinniga@msn.com', 'Coral', 'Wheatley', '5176299057');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('perkybrockville', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'magusnet@me.com', 'Khloe', 'Fountain', '5795751967');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('gwendraethsteed', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'andersbr@live.com', 'Danny', 'Lees', '7704463843');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('gotbudweiser', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'bwcarty@sbcglobal.net',
'Roger', 'Armitage', '6584463537');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('lubsash', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'kudra@yahoo.ca', 'Kobi', 'Molina', '9162049680');
INSERT INTO Users(username, password, email, first_name, last_name, phone_number)
VALUES ('pacifiedunfriendly', '$2b$12$AKYmB6amQIoZK3vUnN33Le7mEZIrqotkaG6XKl0/b5FgoHOxop.hW', 'kidehen@live.com', 'Ricardo', 'Mcdonald', '3833863359');

-- Table: Chat_Group
-- Rows: 14
INSERT INTO Chat_Group(uid, name) VALUES(6, 'Bae-Goals');
INSERT INTO Chat_Group(uid, name) VALUES(2, 'The Herd');
INSERT INTO Chat_Group(uid, name) VALUES(8, 'We Who Shall Not Be Named');
INSERT INTO Chat_Group(uid, name) VALUES(5, 'Turtley Awesome');
INSERT INTO Chat_Group(uid, name) VALUES(11, 'Koalaty Friends');
INSERT INTO Chat_Group(uid, name) VALUES(12, 'Friendchips');
INSERT INTO Chat_Group(uid, name) VALUES(8, 'Kind Of A Big Dill');
INSERT INTO Chat_Group(uid, name) VALUES(8, 'V.I.P.');
INSERT INTO Chat_Group(uid, name) VALUES(10, 'The Musketeers');
INSERT INTO Chat_Group(uid, name) VALUES(10, 'The Avengers');
INSERT INTO Chat_Group(uid, name) VALUES(6, 'Watts Up');
INSERT INTO Chat_Group(uid, name) VALUES(13, 'Ride Or Dies');
INSERT INTO Chat_Group(uid, name) VALUES(5, 'Game of Phones');
INSERT INTO Chat_Group(uid, name) VALUES(6, 'The Chamber of Secrets');

-- Table: Chat_Members
-- Rows: 18
INSERT INTO Chat_Members(cid, uid) VALUES (7, 11);
INSERT INTO Chat_Members(cid, uid) VALUES (7, 6);
INSERT INTO Chat_Members(cid, uid) VALUES (7, 3);
INSERT INTO Chat_Members(cid, uid) VALUES (7, 5);
INSERT INTO Chat_Members(cid, uid) VALUES (7, 2);
INSERT INTO Chat_Members(cid, uid) VALUES (4, 3);
INSERT INTO Chat_Members(cid, uid) VALUES (4, 2);
INSERT INTO Chat_Members(cid, uid) VALUES (6, 12);
INSERT INTO Chat_Members(cid, uid) VALUES (3, 9);
INSERT INTO Chat_Members(cid, uid) VALUES (8, 8);
INSERT INTO Chat_Members(cid, uid) VALUES (9, 8);
INSERT INTO Chat_Members(cid, uid) VALUES (13, 1);
INSERT INTO Chat_Members(cid, uid) VALUES (13, 10);
INSERT INTO Chat_Members(cid, uid) VALUES (8, 6);
INSERT INTO Chat_Members(cid, uid) VALUES (13, 7);
INSERT INTO Chat_Members(cid, uid) VALUES (9, 13);
INSERT INTO Chat_Members(cid, uid) VALUES (2, 2);
INSERT INTO Chat_Members(cid, uid) VALUES (4, 9);

-- Table: Messages
-- Rows: 12
INSERT INTO Messages(cid, uid, message) VALUES (7, 11, 'Lorem ipsum sodales iaculis integer lectus hac, ' ||
 'dictumst vel aenean feugiat lacinia, pretium felis in cubilia non.');
 INSERT INTO Messages(cid, uid, message) VALUES (7, 6, 'At fringilla feugiat conubia varius non aliquam suscipit ' ||
  'varius magna fermentum, cubilia enim duis porta fringilla est tristique lectus mauris nulla vivamus integer ' ||
   'congue fermentum ligula elementum euismod ut senectus a.');
 INSERT INTO Messages(cid, uid, message) VALUES (4, 3, 'Senectus phasellus laoreet felis dolor vitae duis ligula ' ||
  'consequat, adipiscing quam ac nam leo elit class augue, feugiat porttitor tempor libero odio lorem tempus eu ' ||
   'nullam eget nibh risus donec posuere donec.');
 INSERT INTO Messages(cid, uid, message) VALUES (4, 2, 'Mauris diam turpis pellentesque aliquam euismod ' ||
  'condimentum torquent sit arcu, vulputate dictumst mauris fames pulvinar mollis in eleifend placerat, vivamus ' ||
   'tellus nullam ligula sem molestie hendrerit torquent donec fringilla accumsan velit tellus aliquam nulla.');
 INSERT INTO Messages(cid, uid, message) VALUES (6, 12, 'Tempus cursus sapien laoreet velit hendrerit torquent nam.');
 INSERT INTO Messages(cid, uid, message) VALUES (3, 9, 'Lorem ipsum velit maecenas posuere morbi vulputate ' ||
  'facilisis nam, per ligula a id hendrerit integer.');
 INSERT INTO Messages(cid, uid, message) VALUES (8, 8, 'Dui per sodales vitae ad cursus ut imperdiet elementum ' ||
  'pulvinar pellentesque scelerisque conubia netus.');
 INSERT INTO Messages(cid, uid, message) VALUES (9, 8, 'Lorem tellus platea orci porttitor enim sollicitudin.');
 INSERT INTO Messages(cid, uid, message) VALUES (13, 1, 'Posuere ut id lectus velit id sem posuere bibendum ' ||
  'odio turpis, tristique praesent eros elit pellentesque adipiscing lacinia donec.');
 INSERT INTO Messages(cid, uid, message) VALUES (13, 10, 'Id fringilla gravida ac pellentesque fringilla fermentum ' ||
  'augue pulvinar, dui taciti adipiscing potenti maecenas tristique.');
 INSERT INTO Messages(cid, uid, message) VALUES (8, 6, 'Lorem ipsum accumsan rhoncus quisque lacus, diam quisque ' ||
  'sagittis tellus praesent lobortis, sed iaculis curabitur sit.');
 INSERT INTO Messages(cid, uid, message) VALUES (13, 7, 'Nibh quam congue feugiat nam facilisis dapibus primis ' ||
  'lorem mollis purus etiam taciti eros.');

-- Table: Photo
-- Rows: 8
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 3);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 5);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 2);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 10);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 12);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 9);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 7);
INSERT INTO Photo(image, mid) VALUES ('static/img/test_url.jpeg', 6);

-- Table: Replies
-- Rows: 5
INSERT INTO Replies VALUES (9, 10);
INSERT INTO Replies VALUES (10, 12);
INSERT INTO Replies VALUES (7, 11);
INSERT INTO Replies VALUES (1, 2);
INSERT INTO Replies VALUES (3, 4);

-- Table: Vote
-- Rows: 12
INSERT INTO Vote(mid, uid, upvote) VALUES (1, 6, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (1, 11, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (1, 3, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (1, 5, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (1, 2, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (2, 11, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (7, 6, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (11, 8, true);
INSERT INTO Vote(mid, uid, upvote) VALUES (3, 3, false);
INSERT INTO Vote(mid, uid, upvote) VALUES (4, 2, false);
INSERT INTO Vote(mid, uid, upvote) VALUES (8, 8, false);
INSERT INTO Vote(mid, uid, upvote) VALUES (12, 7, false);

-- Table: Contacts
-- Rows: 12
INSERT INTO Contacts VALUES (4, 10);
INSERT INTO Contacts VALUES (6, 3);
INSERT INTO Contacts VALUES (3, 12);
INSERT INTO Contacts VALUES (7, 4);
INSERT INTO Contacts VALUES (10, 5);
INSERT INTO Contacts VALUES (8, 9);
INSERT INTO Contacts VALUES (5, 2);
INSERT INTO Contacts VALUES (2, 5);
INSERT INTO Contacts VALUES (9, 7);
INSERT INTO Contacts VALUES (1, 8);
INSERT INTO Contacts VALUES (11, 10);
INSERT INTO Contacts VALUES (12, 1);

-- Table: Hashtags
-- Rows: 13
INSERT INTO Hashtags(hashtag) VALUES ('#art');
INSERT INTO Hashtags(hashtag) VALUES ('#amazing');
INSERT INTO Hashtags(hashtag) VALUES ('#artist');
INSERT INTO Hashtags(hashtag) VALUES ('#autumn');
INSERT INTO Hashtags(hashtag) VALUES ('#awesome');
INSERT INTO Hashtags(hashtag) VALUES ('#adventure');
INSERT INTO Hashtags(hashtag) VALUES ('#architecture');
INSERT INTO Hashtags(hashtag) VALUES ('#artwork');
INSERT INTO Hashtags(hashtag) VALUES ('#abs');
INSERT INTO Hashtags(hashtag) VALUES ('#aesthetic');
INSERT INTO Hashtags(hashtag) VALUES ('#anime');
INSERT INTO Hashtags(hashtag) VALUES ('#Australia');
INSERT INTO Hashtags(hashtag) VALUES ('#animals');

-- Table: Hashtags_Messages
-- Rows: 14
INSERT INTO Hashtags_messages VALUES (7, 3);
INSERT INTO Hashtags_messages VALUES (10, 8);
INSERT INTO Hashtags_messages VALUES (6, 8);
INSERT INTO Hashtags_messages VALUES (13, 3);
INSERT INTO Hashtags_messages VALUES (10, 12);
INSERT INTO Hashtags_messages VALUES (2, 4);
INSERT INTO Hashtags_messages VALUES (4, 11);
INSERT INTO Hashtags_messages VALUES (4, 4);
INSERT INTO Hashtags_messages VALUES (3, 5);
INSERT INTO Hashtags_messages VALUES (4, 8);
INSERT INTO Hashtags_messages VALUES (5, 4);
INSERT INTO Hashtags_messages VALUES (9, 12);
INSERT INTO Hashtags_messages VALUES (12, 2);
INSERT INTO Hashtags_messages VALUES (7, 2);