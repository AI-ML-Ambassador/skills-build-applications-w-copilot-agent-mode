import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://laughing-space-winner-g45r6vp47rjr3ww4q-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h2 className="text-center my-4">Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Activity</th>
            <th>Duration (minutes)</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.activity}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
