-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.0.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla concerts.bands: ~6 rows (aproximadamente)
INSERT INTO `bands` (`id`, `bandname`, `style`, `email`, `website`) VALUES
	(2, 'Led Zeppelin', 'Rock&Roll', 'led@zeppelin.eus', 'www.stairway-to-heaven.com'),
	(3, 'Thin Lizzy', 'Rock&Roll', 'Thin@lizzy.eus', 'www.the-boys-are-back-in-town.org'),
	(4, 'Abba', 'Pop', 'dancing@queen.eus', 'www.dancing_queen.net'),
	(10, 'Abba2', 'Pop', 'dancing@queen.eus', 'www.the-boys-are-back-intown.net'),
	(15, 'Abba', 'Pop', 'dancing@queen.eus', 'www.dancing_queen.net'),
	(16, 'Abbaq2', 'Pop', 'dancing@queen.eus', 'www.dancing_queen.net');

-- Volcando datos para la tabla concerts.concerts: ~0 rows (aproximadamente)
INSERT INTO `concerts` (`id`, `id_stage`, `id_band`, `id_shift`) VALUES
	(3, 55, 66, 77);

-- Volcando datos para la tabla concerts.users: ~0 rows (aproximadamente)
INSERT INTO `users` (`id`, `login_email`, `passw`, `secret`, `rol`) VALUES
	(1, 'worker@email.es', '1234', '1687426703.252334', 'A');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
