class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM
        
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        training_distance: float = self.get_distance()
        return training_distance / self.duration
                
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    LEN_STEP = 0.65

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при беге."""
        COEF_MULTIPLE = 18
        COEF_MINUS = 20
        mean_speed = super().get_mean_speed()
        MIN_IN_HOUR = 60
        duration_minute = self.duration * MIN_IN_HOUR
        return ((COEF_MULTIPLE * mean_speed - COEF_MINUS)
                / super().M_IN_KM * duration_minute
                )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        
    def get_spent_calories(self) -> float:
        COEF_WEIGHT = 0.035
        COEF_WEIGHT_SPEED = 0.029
        mean_speed = super().get_mean_speed()
        MIN_IN_HOUR = 60
        duration_minute = self.duration * MIN_IN_HOUR
        return ((COEF_WEIGHT * self.weight
                + (mean_speed * mean_speed / self.height)
                * COEF_WEIGHT_SPEED * self.weight)
                * duration_minute
                )
                 
 
class Swimming(Training):
    """Тренировка: плавание."""
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения при плавании."""
        training_distance: float = self.length_pool * self.count_pool
        return training_distance / self.duration

    def get_spent_calories(self) -> float:
        # (средняя_скорость + 1.1) * 2 * вес #
        COEF_ADDITIONAL = 1.1
        COEF_MULTIPL = 2
        mean_speed = self.get_mean_speed()
        return (mean_speed + COEF_ADDITIONAL) * COEF_MULTIPL * self.weight


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
