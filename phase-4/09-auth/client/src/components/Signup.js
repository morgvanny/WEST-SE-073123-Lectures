import { useHistory, Link } from "react-router-dom";
import styled from "styled-components";
import { useFormik } from "formik";
import * as yup from "yup";

function Signup() {
  const history = useHistory();

  const formSchema = yup.object().shape({
    name: yup.string().required("Please enter a user name"),
    email: yup.string().email(),
  });

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      }).then((res) => {
        if (res.ok) {
          res.json().then((user) => {
            history.push("/");
          });
        } else {
          res.json().then(console.log);
        }
      });
    },
  });

  return (
    <>
      <h2 style={{ color: "red" }}> {formik.errors.name}</h2>
      <h2>Sign up here!</h2>
      <h2>Already a member?</h2>
      <Link to="/login">Login</Link>
      <Form onSubmit={formik.handleSubmit}>
        <label htmlFor="name">Username</label>
        <input
          id="name"
          type="text"
          name="name"
          value={formik.values.name}
          onChange={formik.handleChange}
        />
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="text"
          name="email"
          value={formik.values.email}
          onChange={formik.handleChange}
        />
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          name="password"
          value={formik.values.password}
          onChange={formik.handleChange}
        />
        <input type="submit" value="Sign Up!" />
      </Form>
    </>
  );
}

export default Signup;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 400px;
  margin: auto;
  font-family: Arial;
  font-size: 30px;
  input[type="submit"] {
    background-color: #42ddf5;
    color: white;
    height: 40px;
    font-family: Arial;
    font-size: 30px;
    margin-top: 10px;
    margin-bottom: 10px;
  }
`;
