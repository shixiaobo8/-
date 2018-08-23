/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50715
Source Host           : localhost:3306
Source Database       : django_wesure_omsa

Target Server Type    : MYSQL
Target Server Version : 50715
File Encoding         : 65001

Date: 2018-02-22 19:15:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add nav', '7', 'add_nav');
INSERT INTO `auth_permission` VALUES ('20', 'Can change nav', '7', 'change_nav');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete nav', '7', 'delete_nav');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$24000$4Od4ddLDeP5D$QVYhoTJZ84b20VdZru579rci3JS8icB3P5dooAKAOQA=', '2018-02-13 10:18:26.464000', '1', 'v_ygshi', '', '', 'shixiaobo8@163.com', '1', '1', '2018-02-09 08:10:49.657000');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$24000$h3bYzGsxyrFM$oX+Tq87Iv1C6uGjvACDG1cWdDWaNpc6ea0DTunFfs0w=', '2018-02-22 08:13:20.709000', '1', 'admin', '', '', 'admin@163.com', '1', '1', '2018-02-22 08:00:51.197000');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$24000$CPb8G0PHM6nN$HLlpXjylnAU5EimsS7uEcmL7emel/c9I1KNHTJNMCzg=', null, '1', 'wesure', '', '', 'wesure@163.com', '1', '1', '2018-02-22 08:04:48.958000');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-02-09 08:20:43.730000', '1', 'Server Dashboard', '1', 'Added.', '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-02-09 08:23:06.996000', '2', '服务器文件管理', '1', 'Added.', '7', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-02-22 08:15:43.194000', '1', 'Server Dashboard', '2', '已修改 thirdNavName 和 thirdNavUrl 。', '7', '2');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'index', 'nav');
INSERT INTO `django_content_type` VALUES ('8', 'Server', 'wojenkinsservices');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-02-09 08:09:28.653000');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-02-09 08:09:29.077000');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-02-09 08:09:29.162000');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-02-09 08:09:29.179000');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-02-09 08:09:29.250000');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-02-09 08:09:29.292000');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-02-09 08:09:29.332000');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-02-09 08:09:29.340000');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-02-09 08:09:29.375000');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-02-09 08:09:29.377000');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-02-09 08:09:29.386000');
INSERT INTO `django_migrations` VALUES ('12', 'sessions', '0001_initial', '2018-02-09 08:09:29.416000');
INSERT INTO `django_migrations` VALUES ('13', 'index', '0001_initial', '2018-02-09 08:13:02.634000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('v24tlvoufo5b7c7hujtww84yaw8sz6sh', 'ZjUwNGIwNmZhYmZmZDBjMjgyZjI3OWFhZjAzMjMzOWM3YmE5M2ViZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjI0NTYzZTlhMmNjMmZkMDNiMGEwZjVhYTllZWE0MWEzYTI1MWUzMzgiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-02-27 10:18:26.488000');
INSERT INTO `django_session` VALUES ('wy00xdwoapc9qqszqep9m9myyrzkt8nz', 'ZDUyOWM1NDcwMzc4OTYyYjllYTNiZTM3YzQ5MWFhMmZhZjZhZmZiYzp7Il9hdXRoX3VzZXJfaGFzaCI6ImFiZGRlODgzMGFhODJmZDBjZjJmY2VjZGMxZGJhOWM0ZGQxMzBiNWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-03-08 08:13:20.713000');

-- ----------------------------
-- Table structure for index_nav
-- ----------------------------
DROP TABLE IF EXISTS `index_nav`;
CREATE TABLE `index_nav` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstNavName` varchar(40) DEFAULT NULL,
  `firstNavUrl` varchar(40) DEFAULT NULL,
  `firstNavIconName` varchar(40) DEFAULT NULL,
  `secondNavName` varchar(40) DEFAULT NULL,
  `secondNavUrl` varchar(40) DEFAULT NULL,
  `thirdNavName` varchar(40) DEFAULT NULL,
  `thirdNavUrl` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_nav
-- ----------------------------
INSERT INTO `index_nav` VALUES ('1', 'Server Dashboard', '/server/status', 'fa fa-dashboard', '服务器状态列表', '/server/status/list', 'jenkins服务管理', '/server/jenkins/prolist');
INSERT INTO `index_nav` VALUES ('2', '服务器文件管理', '/file', 'fa fa-files-o', '服务器文件列表', '/file/upload', '', '');

-- ----------------------------
-- Table structure for wo_jenkins_services
-- ----------------------------
DROP TABLE IF EXISTS `wo_jenkins_services`;
CREATE TABLE `wo_jenkins_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `service_name` varchar(255) DEFAULT '' COMMENT '服务名',
  `locate_service_name` varchar(255) DEFAULT '' COMMENT '本地服务名',
  `project_name` varchar(255) DEFAULT '' COMMENT '所属产品',
  `service_app_name` varchar(255) DEFAULT '' COMMENT '服务启动名称',
  `is_bin` int(255) DEFAULT '0' COMMENT '有(无)bin目录,0无,1表示有',
  `is_config` int(255) DEFAULT '0' COMMENT '是否含有配置有文件,0表示无,1表示有',
  `sup_group` varchar(255) DEFAULT '1' COMMENT 'supvisor表中的是否的所属分类',
  `suffix` varchar(255) DEFAULT '0' COMMENT '开发语言(可执行程序文件的后缀名),0无后缀表示golang,1jar表示java程序',
  `service_dir` varchar(255) DEFAULT '' COMMENT '服务部署目录',
  `ctime` datetime DEFAULT NULL COMMENT '创建时间',
  `mtime` datetime DEFAULT NULL COMMENT '最后一次修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of wo_jenkins_services
-- ----------------------------
INSERT INTO `wo_jenkins_services` VALUES ('1', 'frontend-api', 'health-frontend-api', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('2', 'health-frontend-api-v2', 'health-frontend-api-v2', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('3', 'insure-service', 'health-insure-service', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('4', 'health-insure-service-v2', 'health-insure-service-v2', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('5', 'health-promotion-dental-service', 'health-promotion-dental-service', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('6', 'health-promotion-dental-gateway', 'health-promotion-dental-gateway', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('7', 'promotion-werun-service', 'promotion-werun-service', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('8', 'promotion-invite', 'promotion-invite', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('9', 'order-service', 'order-service', 'nh', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('10', 'wesure-gateway', 'wesure-gateway', 'nh', 'wesure-gateway-web-0.0.1-SNAPSHOT.jar', '0', '0', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('11', 'policy-service', 'policy-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('12', 'policy-oss-service', 'policy-oss-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('13', 'order-pay-service', 'order-pay-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('14', 'media-service', 'media-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('15', 'coupon-service', 'coupon-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('16', 'claim-service', 'claim-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('17', 'underwriting-service', 'underwriting-service', 'public', 'app', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('18', 'usernotify', 'usernotify', 'common', 'usernotify', '1', '1', 'policydata', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('19', 'orderinfo', 'orderinfo', 'car', 'orderinfo', '1', '1', 'policydata', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('20', 'usergift', 'usergift', 'car', 'usergift', '1', '1', 'policydata', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('21', 'gift-account-service', 'gift-account-service', 'car', 'gift-account-service', '0', '1', 'No', 'No', '/usr/local/wesure/common-service', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('22', 'carpolicyapp', 'carpolicyapp', 'fa', 'carpolicyapp', '1', '1', 'policyapp', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('23', 'carorderapp', 'carorderapp', 'fa', 'carorderapp', '1', '1', 'policyapp', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('24', 'cargiftapp', 'cargiftapp', 'fa', 'cargiftapp', '1', '1', 'policyapp', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('25', 'activity-api', 'activity-api', 'public', 'activity-api', '0', '1', 'activity-group', 'No', '/usr/local/wesure/common-service', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('26', 'activity-service', 'activity-service', 'da', 'activity-service', '0', '1', 'activity-group', 'No', '/usr/local/wesure/common-service', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('27', 'cdk-stock-service', 'cdk-stock-service', 'da', 'cdk-stock-service', '0', '1', 'activity-group', 'No', '/usr/local/wesure/common-service', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('28', 'wesure-lottery-b', 'wesure-lottery-b', 'public', 'wesure-lottery-b.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('29', 'wesure-lottery-s', 'wesure-lottery-s', 'public', 'wesure-lottery-s.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('30', 'wesure-activity-s', 'wesure-activity-s', 'public', 'wesure-activity-s.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('31', 'wesure-ship-shipserver-s', 'wesure-ship-shipserver-s', 'public', 'wesure-ship-shipserver-s.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('32', 'lmplatform-service', 'lmplatform-service', 'publi', 'lmplatform-service', '0', '1', 'activity-group', 'No', '/usr/local/wesure/common-service', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('33', 'pricinggift-service', 'pricinggift-service', 'fa', 'pricinggift-service', '0', '1', 'activity-group', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('34', 'wesure-car-owner', 'wesure-car-owner', 'public', 'wesure-car-owner.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('35', 'wesure-car-superman', 'wesure-car-superman', 'da', 'wesure-car-superman-web-0.0.1-SNAPSHOT.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('36', 'wesure-gift-supplier', 'wesure-gift-supplier', 'public', 'wesure-gift-supplier.jar', '1', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('37', 'wesure-score', 'wesure-score', 'common', 'wesure-score.jar', '0', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('38', 'wesure-score-admin', 'wesure-score-admin', 'common', 'wesure-score-admin.jar', '0', '1', 'No', 'jar', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('39', 'wesure-car-application', 'car', 'at', 'current', '0', '0', 'No', 'war', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('40', 'wesure-link', 'link', 'at', 'current', '0', '0', 'No', 'war', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('41', 'wesure-notify', 'notify', 'at', 'current', '0', '0', 'No', 'war', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('42', 'car-frontend-api', 'car-frontend-api', 'da', 'car-frontend-api', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy/cargasapp', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('43', 'cargasserver', 'cargasserver', 'da', 'cargasserver', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy/cargasapp', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('44', 'cargasbatch', 'cargasbatch', 'da', 'cargasbatch', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy/cargasapp', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('45', 'cargasstats', 'cargasstats', 'da', 'cargasstats', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy/cargasapp', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('46', 'wxapp_api', 'wxapp_api', 'public', 'wxapp_api', '1', '1', 'wxpush-group', 'No', '/usr/local/wesure/common-service/interface', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('47', 'wxapp_push', 'wxapp_push', 'public', 'wxapp_push', '1', '1', 'wxpush-group', 'No', '/usr/local/wesure/common-service/interface', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('48', 'wxapi', 'wxapi', 'public', 'wxapi', '1', '1', 'wxpush-group', 'No', '/usr/local/wesure/common-service/interface', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('49', 'wxpush', 'wxpush', 'public', 'wxpush', '1', '1', 'wxpush-group', 'No', '/usr/local/wesure/common-service/interface', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('50', 'webapi', 'webapi', 'common', 'webapi', '1', '1', 'carpolicy', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('51', 'userapp', 'userapp', 'common', 'userapp', '1', '1', 'datauser', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('52', 'userprofile', 'userprofile', 'common', 'userprofile', '1', '1', 'datauser', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('53', 'subcribe-redpkg', 'subcribe-redpkg', 'common', 'subcribe-redpkg', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('54', 'subscribe', 'subscribe', 'common', 'subscribe', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('55', 'subscribe-v2', 'subscribe-v2', 'common', 'subscribe-v2', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('56', 'redpoint', 'redpoint', 'common', 'redpoint', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('57', 'white_redpacket', 'white_redpacket', 'common', 'white_redpacket', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('58', 'travel-insure-service', 'travel-insure-service', 'travel', 'travel-insure-service', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('59', 'travel-gateway', 'travel-gateway', 'travel', 'travel-gateway', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('60', 'travel-frontend-api', 'travel-frontend-api', 'travel', 'travel-frontend-api', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('61', 'air-union-gateway', 'air-union-gateway', 'travel', 'air-union-gateway', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('62', 'cargateway', 'cargateway', 'fa', 'cargateway', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('63', 'carmgrapp', 'carmgrapp', 'fa', 'carmgrapp', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('64', 'carquoteapp', 'carquoteapp', 'fa', 'carquoteapp', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('65', 'carinsureapp', 'carinsureapp', 'fa', 'carinsureapp', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('66', 'carmgrdata', 'carmgrdata', 'fa', 'carmgrdata', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('67', 'carquotedata', 'carquotedata', 'fa', 'carquotedata', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('68', 'carinsuredata', 'carinsuredata', 'fa', 'carinsuredata', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('69', 'carsentryapp', 'carsentryapp', 'fa', 'carsentryapp', '0', '1', 'No', 'No', '/usr/local/wesure/carpolicy', '2018-02-22 19:06:37', '2018-02-22 19:06:37');
INSERT INTO `wo_jenkins_services` VALUES ('70', 'wesure-inf-service', 'wesure-inf-service', 'public', 'wesure-inf-service', '0', '1', 'No', 'No', '/usr/local/wesure', '2018-02-22 19:06:37', '2018-02-22 19:06:37');

-- ----------------------------
-- Table structure for wo_supervisor_group
-- ----------------------------
DROP TABLE IF EXISTS `wo_supervisor_group`;
CREATE TABLE `wo_supervisor_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `supervisor_group_name` varchar(255) DEFAULT 'No' COMMENT 'supervisor组类别名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='supervisor组类别名称';

-- ----------------------------
-- Records of wo_supervisor_group
-- ----------------------------
INSERT INTO `wo_supervisor_group` VALUES ('1', 'No');
INSERT INTO `wo_supervisor_group` VALUES ('2', 'activity-group');
INSERT INTO `wo_supervisor_group` VALUES ('3', 'carpolicy');
INSERT INTO `wo_supervisor_group` VALUES ('4', 'datauser');
INSERT INTO `wo_supervisor_group` VALUES ('5', 'wxpush-group');
