import axios from 'axios';

document.addEventListener('DOMContentLoaded', () => {
    function getThresholdValues() {
        const yellowThresholdInput = document.getElementById('yellow-threshold');
        const redThresholdInput = document.getElementById('red-threshold');

        const yellowThreshold = yellowThresholdInput ? parseFloat(yellowThresholdInput.value) || 0.6 : 0.6;
        const redThreshold = redThresholdInput ? parseFloat(redThresholdInput.value) || 0.8 : 0.8;
        return { yellowThreshold, redThreshold };
    }

    function getCellClass(coefficient) {
        const { yellowThreshold, redThreshold } = getThresholdValues();

        if (coefficient > redThreshold) {
            return 'red-row';
        } else if (coefficient > yellowThreshold) {
            return 'yellow-row';
        } else {
            return 'green-row';
        }
    }

    function fetchUserData() {
        const userId = new URLSearchParams(window.location.search).get('id');
        axios.get(`/get/user/${userId}`)
            .then(response => {
                const userData = response.data;
                const users = userData.table;

                const userHeader = document.getElementById('user-header');
                userHeader.textContent = `ID пользователя: ${userData.id_user} | ${userData.name}`;

                const homeworkIds = users[0].coefficients.map(item => item.id_homework);

                const thead = document.querySelector('#coefficients-table thead tr');
                thead.innerHTML = '<th>ID задания / ID студента</th>';
                homeworkIds.forEach(id => {
                    const th = document.createElement('th');
                    th.textContent = `ДЗ ${id}`;
                    thead.appendChild(th);
                });

                const tbody = document.querySelector('#coefficients-table-body');
                tbody.innerHTML = '';

                users.forEach(user => {
                    const row = document.createElement('tr');

                    const idCell = document.createElement('td');
                    const link = document.createElement('a');
                    link.href = `http://127.0.0.1:8080/user/?id=${user.id_user}`;
                    link.textContent = user.id_user;
                    link.classList.add('user-link-cell');
                    idCell.appendChild(link);
                    row.appendChild(idCell);

                    const userCoefficients = user.coefficients.map(item => item.coefficient);
                    homeworkIds.forEach(id => {
                        const td = document.createElement('td');
                        const coefficient = userCoefficients.find((_, index) => user.coefficients[index]?.id_homework === id) || '-';

                        if (typeof coefficient === 'number') {
                            td.className = getCellClass(coefficient);
                        }

                        td.textContent = coefficient;
                        row.appendChild(td);
                    });

                    tbody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }

    const yellowThresholdInput = document.getElementById('yellow-threshold');
    const redThresholdInput = document.getElementById('red-threshold');
    if (yellowThresholdInput && redThresholdInput) {
        yellowThresholdInput.addEventListener('input', fetchUserData);
        redThresholdInput.addEventListener('input', fetchUserData);
    }

    fetchUserData();
});
