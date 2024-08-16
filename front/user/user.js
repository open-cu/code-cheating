import { coefficients } from '../mocks/coefficients.js';

document.addEventListener('DOMContentLoaded', () => {
    function fetchUserData() {
        const users = coefficients.table;

        const userHeader = document.getElementById('user-header');
        userHeader.textContent = `ID пользователя: ${coefficients.id_user} | ${coefficients.name}`;

        const homeworkIds = users[0].coefficients.map(item => item.id_homework);

        const thead = document.querySelector('#coefficients-table thead tr');
        thead.innerHTML = '<th>ID задания / ID студента</th>';
        homeworkIds.forEach(id => {
            const th = document.createElement('th');
            th.textContent = `ДЗ ${id}`;
            thead.appendChild(th);
        });

        function getRowClass(user) {
            const sum = user.coefficients.reduce((acc, item) => acc + item.coefficient, 0);

            if (sum > 8) {
                return 'red-row';
            } else if (sum > 7) {
                return 'yellow-row';
            } else {
                return 'green-row';
            }
        }

        const tbody = document.querySelector('#coefficients-table-body');
        users.forEach(user => {
            const row = document.createElement('tr');
            row.className = getRowClass(user);

            const idCell = document.createElement('td');
            idCell.textContent = user.id_user;
            row.appendChild(idCell);

            const userCoefficients = user.coefficients.map(item => item.coefficient);
            homeworkIds.forEach(id => {
                const td = document.createElement('td');
                const coefficient = userCoefficients.find((_, index) => user.coefficients[index]?.id_homework === id) || '-';
                td.textContent = coefficient;
                row.appendChild(td);
            });

            tbody.appendChild(row);
        });
    }

    fetchUserData();
});
