import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/Home";
import How from "../pages/How"
import Contact from "../pages/Contact"
import Services from "../pages/Services"
import Login from "../pages/Login"
import Layout from "../components/Layout";
import Packages from "../pages/Packages";



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
            path:"/packages",
            element:<Packages/>
        },
        {
            path:"/how",
            element:<How/>
        },
        {
            path:"/services",
            element:<Login/>
        },
        {
            path:"/contact",
            element:<Contact/>
        },
        {
            path:"/login",
            element:<Login/>
        }
    ]
   }
])