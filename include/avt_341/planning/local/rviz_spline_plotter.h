//
// Created by stefan on 2021-08-19.
//

#ifndef AVT_341_RVIZ_SPLINE_PLOTTER_H
#define AVT_341_RVIZ_SPLINE_PLOTTER_H

#include "avt_341/planning/local/spline_plotter.h"
#include "avt_341/visualization/base_visualizer.h"
#include "avt_341/node/ros_types.h"
#include "avt_341/node/node_proxy.h"

namespace avt_341 {
  namespace planning{

    class RVIZPlotter : public Plotter {
    public:
      RVIZPlotter(std::shared_ptr<avt_341::visualization::VisualizerBase> visualizer, std::shared_ptr<avt_341::node::NodeProxy> node);
      virtual void Display(bool save, const std::string & ofname, int nx, int ny) override;

    private:
      avt_341::msg::Marker get_marker_msg(bool is_blocked) const;
      std::shared_ptr<avt_341::node::NodeProxy> node_;
      std::shared_ptr<avt_341::node::Publisher<avt_341::msg::Marker>> candidate_paths_publisher;
      std::shared_ptr<avt_341::node::Publisher<avt_341::msg::Marker>> blocked_paths_publisher;
    };
  } // namespace planning
} // namespace avt_341

#endif //AVT_341_RVIZ_SPLINE_PLOTTER_H