import {
  FileText,
  FileTextIcon,
  ShieldCheck,
  ShieldCheckIcon,
  UserCheck,
  UserCheckIcon,
  Users,
  UsersIcon,
  Workflow,
  WorkflowIcon,
} from "lucide-react";
import React, { useEffect, useState } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";

const colors = [
  {
    id: 1,
    border: "border-l-blue-500",
    text: "text-blue-500",
    bg: "bg-blue-50",
  },
  {
    id: 2,
    border: "border-l-indigo-500",
    text: "text-indigo-500",
    bg: "bg-indigo-50",
  },
  {
    id: 3,
    border: "border-l-violet-500",
    text: "text-violet-500",
    bg: "bg-violet-50",
  },
  {
    id: 4,
    border: "border-l-teal-500",
    text: "text-teal-500",
    bg: "bg-teal-50",
  },
  {
    id: 5,
    border: "border-l-cyan-500",
    text: "text-cyan-500",
    bg: "bg-cyan-50",
  },
  { id: 6, border: "border-l-sky-500", text: "text-sky-500", bg: "bg-sky-50" },
  {
    id: 7,
    border: "border-l-emerald-500",
    text: "text-emerald-500",
    bg: "bg-emerald-50",
  },
  {
    id: 8,
    border: "border-l-slate-500",
    text: "text-slate-500",
    bg: "bg-slate-50",
  },
  {
    id: 9,
    border: "border-l-purple-500",
    text: "text-purple-500",
    bg: "bg-purple-50",
  },
  {
    id: 10,
    border: "border-l-blue-700",
    text: "text-blue-700",
    bg: "bg-blue-50",
  },
  {
    id: 11,
    border: "border-l-teal-700",
    text: "text-teal-700",
    bg: "bg-teal-50",
  },
  {
    id: 12,
    border: "border-l-indigo-700",
    text: "text-indigo-700",
    bg: "bg-indigo-50",
  },
];

const Division = ({ divisionName, index }) => {
  const navigate = useNavigate();
  const cards = [
    {
      title: "Entitlement",
      icon: <ShieldCheckIcon size={36} />,
      color: "from-purple-400 to-indigo-500",
    },
    {
      title: "Policy",
      icon: <FileTextIcon size={36} />,
      color: "from-blue-400 to-cyan-500",
    },
    {
      title: "Workflow",
      icon: <WorkflowIcon size={36} />,
      color: "from-green-400 to-emerald-500",
    },
    {
      title: "Spocs",
      icon: <UsersIcon size={36} />,
      color: "from-pink-400 to-rose-500",
    },
    {
      title: "Approver",
      icon: <UserCheckIcon size={36} />,
      color: "from-yellow-400 to-orange-500",
    },
  ];

  const handleClick = () => {
    navigate(`/${divisionName}`);
  };

  const colorIndex = typeof index === "number" ? index % colors.length : 0;
  const color = colors[colorIndex];   
  return (
    <div onClick={handleClick}>
      <div
        className={`group relative ${
          color.bg
        } rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1 p-6 flex flex-col items-center justify-center gap-2 border ${
          color.border
        } cursor-pointer`}
      >
          <span
            className={` ${
              color.text
            } group-hover:text-purple-700 font-bold text-lg transition-colors duration-300`}
          >
            {divisionName}
          </span>
      </div>
    </div>

    // <div className="w-full min-h-screen bg-gray-50 p-2">
    //   {/* Header */}
    //   <div className="text-center mb-10">
    //     <h1 className="text-2xl font-bold text-gray-700 uppercase tracking-widest">
    //       {divisionName}
    //     </h1>
    //     <div className="mx-auto mt-3 h-1 w-12 rounded-full bg-indigo-500" />
    //   </div>

    //   {/* Cards */}
    //   <div className="grid grid-cols-2 sm:grid-cols-3 gap-5 max-w-3xl mx-auto">
    //     {cards.map((card, index) => (

    //       <div
    //         key={index}
    //         className="bg-white rounded-xl shadow-sm hover:shadow-md border border-gray-100 p-6 flex flex-col items-center gap-3 cursor-pointer hover:-translate-y-1 transition-all duration-200"
    //         onClick={()=>handleChangeRouteCard(card.title)}
    //       >
    //         {/* Icon */}
    //         <div
    //           className={`bg-gradient-to-br ${card.color} text-white rounded-full p-3`}
    //         >
    //           {card.icon}
    //         </div>

    //         {/* Title */}
    //         <p className="text-gray-700 font-semibold text-sm">{card.title}</p>
    //       </div>

    //     ))}
    //   </div>

    //   <div className="flex justify-end my-8 ">
    //     <Link to="/">
    //       <button className="bg-purple-500 rounded px-3 py-3 font-bold text-white hover:hover:-translate-y-1 transition-all duration-200">
    //         Back to Previous
    //       </button>
    //     </Link>
    //   </div>
    // </div>
  );
};

export default Division;
