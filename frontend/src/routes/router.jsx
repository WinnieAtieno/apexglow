import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/Home"
import Login from "../pages/Login"
import Layout from "../components/Layout";



export const router= createBrowserRouter([
   {
    path:"/",
    element:<Layout/>,
    children: [
        {
            index:true,
            element:<Home/>
        },
        {
            path:"/login",
            element:<Login/>
        }
    ]
   }
])