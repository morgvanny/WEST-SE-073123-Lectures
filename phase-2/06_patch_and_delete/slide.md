---
presentation:
  width: 1500
  height: 1000
  controls: false
---

<!-- slide -->

<h2><strong> 🪡 PATCH & DELETE ❌ </strong></h2>

<!-- slide -->

<h2><strong> ✅ Objectives </strong></h2>

- Observe how to send `PATCH` & `DELETE` requests in React
- Review updating parent state via Inverse Data Flow

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Review changes to the project showcase application </strong></h2>

- Observe the `ProjectEditForm` component

- Observe the edit button added to `ProjectListItem` component

- Observe the updates applied in the `App` component

- Update the `useEffect` inside the `ProjectEditForm` component so that the side effect will run upon `projectId` updates

<br>

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Submit the edit project form and make a PATCH request</strong></h2>

<br>

- Inside of the `ProjectEditForm` component, update `handleSubmit` to include a `PATCH` request

- Include the updated state values in the `PATCH` request

- Update the `projects` state in the parent component `App` using the `.map` function

  - The goal is to return a new array with the original project excluded and the newly updated project included

- Reset the edit form after submission is complete

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Click the delete button and make a DELETE request </strong></h2>

<br>

- Attach an `onClick` event listener to the delete button

- Add a `DELETE` fetch request to the event handler for the delete button

- Update the `projects` state in the parent component `App` using the `.filter` function

  - The goal is to return a new array with the deleted project excluded

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Click the claps button and persist the updated number of claps </strong></h2>

<br>

- Send a `PATCH` request when the `clapsCount` is updated through a click event

- Update the `projects` state in the parent component `App` using the `.map` function