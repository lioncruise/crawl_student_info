CREATE TABLE `student` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `birthday` varchar(255) DEFAULT NULL,
  `school` varchar(255) DEFAULT NULL,
  `institute` varchar(255) DEFAULT NULL,
  `id_no` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `hometown` varchar(255) DEFAULT NULL,
  `student_no` varchar(255) DEFAULT NULL,
  `avatar_url` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `degree` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `family` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15706 DEFAULT CHARSET=utf8;